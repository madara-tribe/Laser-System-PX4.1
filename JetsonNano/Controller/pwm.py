import sys
import cv2
import time
import threading
import numpy as np
from .utils.dist_calcurator import prams_calcurator
from .utils.util import letterbox, preprocess, onnx_inference, post_process
from .utils.tools import Tmpfile
from .pwms.PCA9685 import ServoController
import onnxruntime


def onnx_setup(opt):
    cuda = False if opt.cpu=='True' else True
    providers = ['CUDAExecutionProvider', 'CPUExecutionProvider'] if cuda else ['CPUExecutionProvider']
    session = onnxruntime.InferenceSession(opt.onnx_path, providers=providers)

    IN_IMAGE_H = session.get_inputs()[0].shape[2]
    IN_IMAGE_W = session.get_inputs()[0].shape[3]
    new_shape = (IN_IMAGE_W, IN_IMAGE_H)
    return session, new_shape

def inference_(frame, session, new_shape, conf_thres):
    ori_images = [frame.copy()]
    resized_image, ratio, dwdh = letterbox(frame, new_shape=new_shape, auto=False)
    input_tensor = preprocess(resized_image)
    outputs = onnx_inference(session, input_tensor)
    pred_output, Xcoordinate, Ycoordinate, range_ = post_process(outputs, ori_images, ratio, dwdh, conf_thres)
    return pred_output, Xcoordinate, Ycoordinate, range_


class CSI_Camera:
    def __init__(self):
        # Initialize instance variables
        # OpenCV video capture element
        self.video_capture = None
        # The last captured image from the camera
        self.frame = None
        self.grabbed = False
        # The thread where the video capture runs
        self.read_thread = None
        self.read_lock = threading.Lock()
        self.running = False
        
    def open(self, gstreamer_pipeline_string):
        try:
            self.video_capture = cv2.VideoCapture(
                gstreamer_pipeline_string, cv2.CAP_GSTREAMER
            )
            # Grab the first frame to start the video capturing
            self.grabbed, self.frame = self.video_capture.read()

        except RuntimeError:
            self.video_capture = None
            print("Unable to open camera")
            print("Pipeline: " + gstreamer_pipeline_string)


    def start(self):
        if self.running:
            print('Video capturing is already running')
            return None
        # create a thread to read the camera image
        if self.video_capture != None:
            self.running = True
            self.read_thread = threading.Thread(target=self.updateCamera)
            self.read_thread.start()
        return self

    def stop(self):
        self.running = False
        # Kill the thread
        self.read_thread.join()
        self.read_thread = None

    def updateCamera(self):
        # This is the thread to read images from the camera
        while self.running:
            try:
                grabbed, frame = self.video_capture.read()
                with self.read_lock:
                    self.grabbed = grabbed
                    self.frame = frame
            except RuntimeError:
                print("Could not read image from camera")
        # FIX ME - stop and cleanup thread
        # Something bad happened

    def read(self):
        with self.read_lock:
            frame = self.frame.copy()
            grabbed = self.grabbed
        return grabbed, frame

    def release(self):
        if self.video_capture != None:
            self.video_capture.release()
            self.video_capture = None
        # Now kill the thread
        if self.read_thread != None:
            self.read_thread.join()


"""
gstreamer_pipeline returns a GStreamer pipeline for capturing from the CSI camera
Flip the image by setting the flip_method (most common values: 0 and 2)
display_width and display_height determine the size of each camera pane in the window on the screen
Default 1920x1080
"""


def gstreamer_pipeline(sensor_id, hyp):
    return (
        "nvarguscamerasrc sensor-id=%d ! "
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            hyp['capture_width'],
            hyp['capture_height'],
            hyp['framerate'],
            hyp['flip_method'],
            hyp['display_width'],
            hyp['display_height'],
        )
    )

def run_cameras(opt, hyp):
    window_title = "Dual CSI Cameras"
    session, new_shape = onnx_setup(opt)
    disparity = None
    Wmax = hyp['width_angle_max']
    Wmin = hyp['width_angle_min']
    Hmax = hyp['height_angle_max']
    Hmin = hyp['height_angle_min']
    DWidth = hyp['display_width']
    left_camera = CSI_Camera()
    left_camera.open(
        gstreamer_pipeline(
            sensor_id=0, hyp=hyp)
    )
    left_camera.start()

    #right_camera = CSI_Camera()
    #right_camera.open(
    #    gstreamer_pipeline(
    #        sensor_id=1, hyp=hyp)
    #)
    #right_camera.start()
    RdegX, RdegY = int((Wmax+Wmin)/2), int((Hmax+Hmin)/2)
    plotpos = 90
    Controller = ServoController()
    CHANNELS = [hyp['width_cannel'], hyp['height_cannel']]
    Controller.initialize(CHANNELS[0], RdegX)
    Controller.initialize(CHANNELS[1], RdegY)
    time.sleep(2)
    if left_camera.video_capture.isOpened(): #and right_camera.video_capture.isOpened():

        cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)
        Ls = []
        try:
            while True:
                _, left_image = left_camera.read()
                Ls.append(left_image)
                #_, right_image = right_camera.read()
                if len(Ls)==opt.per_frames:
                    Routput, Rx, Ry, Rrange = inference_(Ls[-1], session, new_shape, opt.conf_thres)
                    camera_images = Routput[0] 
                    if disparity is None:
                        #Loutput, Lx, Ly, Lrange = inference_(Rs[-1], session, new_shape, conf_thres)
                    #if abs(Rx-Lx) >=0 or Lx < Rrange or Rx < Lrange:
                        #disp = abs(Rx-Lx)
                        disparity = 25 #disp if disp <= max_disp and disp > min_disp else None
                    else:
                        h, w = camera_images.shape[:2]
                        Rdist, RdegX, RdegY = prams_calcurator(disparity, x=Rx, y=Ry)
                        Rtexts = 'RdegX:{}[V], RdegY : {}[V]'.format(RdegX, RdegY)
                        rframe = cv2.circle(Routput[0], (int(Rx), int(Ry)), 20, (0, 255, 255), 2)
                        cv2.putText(rframe, Rtexts, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, [225, 255, 255], thickness=2)
                        camera_images = rframe
                        #  width
                        if int(RdegX) < 130 and int(RdegX) > 60:
                            Controller.update_pos(CHANNELS[0], RdegX)
                            print("RdegX", RdegX)
                        # height
                        if int(RdegY)<130 and int(RdegY) >60:
                            Controller.update_pos(CHANNELS[1], RdegY)
                            print("RdegY", RdegY)

                    for i in range(0, DWidth, 30):
                        cv2.putText(camera_images, str(int(i/(DWidth/180))), (i, plotpos), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), thickness=1)
                    cv2.imshow(window_title, camera_images)
                    #print(camera_images.shape)
                    Ls = []
                    keyCode = cv2.waitKey(30) & 0xFF
                    if keyCode == 27:
                        break
        finally:
            left_camera.stop()
            left_camera.release()
          #  right_camera.stop()
         #   right_camera.release()
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to open both cameras")
        left_camera.stop()
        left_camera.release()
        #right_camera.stop()
        #right_camera.release()
