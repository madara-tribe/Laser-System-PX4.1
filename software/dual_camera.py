import sys
import cv2
import numpy as np
import time
from .csicam_pipeline import CSI_Camera, gstreamer_pipeline
    
def create_csicams(hyp, sensor_id):
    csi_camera = CSI_Camera()
    csi_camera.open(
        gstreamer_pipeline(
            sensor_id=sensor_id,
            capture_width=hyp['capture_width'],
            capture_height=hyp['capture_height'],
            flip_method=0,
            display_width=hyp['display_width'],
            display_height=hyp['display_height'],
        )
    )
    return csi_camera


class DualCamera(object):
    def __init__(self, opt, hyp):
        self.TIMEOUT = opt.frame_interval
        self.count = 0
        self.Rstack = self.Lstack = []
        self.left_camera = create_csicams(hyp, sensor_id=0)
        self.right_camera = create_csicams(hyp, sensor_id=1)
        self.run_dual_cam(opt, hyp)

    def frame_reset(self):
        self.Rstack = []
        self.Lstack = []
        self.count = 0
    
    
    def run_dual_cam(self, opt, hyp):
        window_title = "Dual CSI Cameras"
        # left csi camera
        self.left_camera.start()
        # right camera
        self.right_camera.start()
        if self.left_camera.video_capture.isOpened() and self.right_camera.video_capture.isOpened():
            cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)
            try:
                while True:
                    _, frameR = self.right_camera.read()
                    _, frameL = self.left_camera.read()
                    if frameL is None or frameR is None:
                        continue
                    # Use numpy to place images next to each other
                    camera_images = np.hstack((frameR, frameL)) 
                    self.count += 0.01
                    if (time.time() - self.count) > self.TIMEOUT:
                    #if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                        self.frame_reset()
                        if opt.plot:
                            cv2.imshow(window_title, camera_images)
                        elif opt.dual:
                            break
                        # This also acts as
                        keyCode = cv2.waitKey(30) & 0xFF
                        # Stop the program on the ESC key
                        if keyCode == 27:
                            break
            finally:        
                self.left_camera.stop()
                self.left_camera.release()
                self.right_camera.stop()
                self.right_camera.release()
                cv2.destroyAllWindows()
        else:
            print('unable to open cameras')
            self.left_camera.stop()
            self.left_camera.release()
            self.right_camera.stop()
            self.right_camera.release()
            cv2.destroyAllWindows()

