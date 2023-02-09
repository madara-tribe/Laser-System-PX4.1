import time
import cv2
import numpy as np
import onnxruntime
from .yolov7.common import letterbox, preprocess, onnx_inference, post_process
from .yolov7.dist_calcurator import prams_calcurator
from .tools import CPULog
    
def load_caps(vid_path, start_time):
    capR = cv2.VideoCapture(vid_path)
    capR.set(cv2.CAP_PROP_POS_FRAMES, start_time * 30)
    return capR

def inference_(frame, session, new_shape, conf_thres):
    ori_images = [frame.copy()]
    resized_image, ratio, dwdh = letterbox(frame, new_shape=new_shape, auto=False)
    input_tensor = preprocess(resized_image)
    outputs = onnx_inference(session, input_tensor)
    pred_output, coordinate_x, coordinate_y, range = post_process(outputs, ori_images, ratio, dwdh, conf_thres)
    return pred_output, coordinate_x, coordinate_y, range
    

class VideoInference:
    def __init__(self, opt): #, udp_client):
        # call CPU burden log writer
        self.logwriter = CPULog()
        start_time = 0
        self.opt = opt
        self.disparity = None
        self.max_disp = opt.max_disparity
        self.min_disp = opt.min_disparity
        self.capR = load_caps(vid_path=opt.rvid_path, start_time=start_time)
        self.capL = load_caps(vid_path=opt.lvid_path, start_time=start_time)
        self.onnx_setup(opt)
        
    def onnx_setup(self, opt):
        cuda = False if opt.cpu=='True' else True
        providers = ['CUDAExecutionProvider', 'CPUExecutionProvider'] if cuda else ['CPUExecutionProvider']
        self.session = onnxruntime.InferenceSession(opt.onnx_path, providers=providers)

        IN_IMAGE_H = self.session.get_inputs()[0].shape[2]
        IN_IMAGE_W = self.session.get_inputs()[0].shape[3]
        self.new_shape = (IN_IMAGE_W, IN_IMAGE_H)
    
    def inference(self):
        Rstack = []
        Lstack = []
        cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
        c = 0
        while self.capR.isOpened() and self.capL.isOpened():
            try:
                retR, frame_right = self.capR.read()
                retL, frame_left = self.capL.read()
                Rstack.append(frame_right)
                Lstack.append(frame_left)
                if not retR and not retL:
                    break
            except Exception as e:
                print(e)
                continue
            if len(Rstack)==self.opt.per_frames and len(Lstack)==self.opt.per_frames:
                # inference each frame
                Routput, Rx, Ry, Rrange = inference_(Rstack[-1], self.session, self.new_shape, self.opt.conf_thres)
                
                frames = Routput[0] #np.concatenate((Routput[0], Loutput[0]), axis=1)
                if self.disparity is None:
                    """
                    disparity is used by right and left camera.
                    distanceand disparity are fixed after calcurate once.
                    """
                    Loutput, Lx, Ly, Lrange = inference_(Lstack[-1], self.session, self.new_shape, self.opt.conf_thres)
                    if abs(Rx-Lx) >=0 or Lx < Rrange or Rx < Lrange:
                        disp = abs(Rx-Lx)
                        self.disparity = disp if disp <= self.max_disp and disp > self.min_disp else None
                else:
                    """
                    without disparity, use only right camera for x, y coordinate
                    """
                    h, w = frames.shape[:2]
                    Rdist, RdcX, RdcY = prams_calcurator(self.disparity, x=Rx, y=Ry)
                    Rtexts = 'distance(z):{}, RdcX:{}[V], RdcY : {}[V]'.format(Rdist, RdcX, RdcY)
                    #Ldist, LdcX, LdcY = prams_calcurator(disparity, x=Lx, y=Ly)
                    #Ltexts = 'distance(z):{}, LdcX:{}[V], LdcY : {}[V]'.format(Ldist, LdcX, LdcY)
                    rframe = cv2.circle(Routput[0], (int(Rx), int(Ry)), 20, (0, 255, 255), 2)
                    cv2.putText(rframe, Rtexts, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, [225, 255, 255], thickness=2)
                    #lframe = cv2.circle(Loutput[0], (int(Lx), int(Ly)), 20, (0, 255, 255), 2)
                    #cv2.putText(lframe, Ltexts, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, [225, 255, 255], thickness=2)
                    frames = rframe # np.concatenate((rframe, lframe), axis=1)
                    
                cv2.imshow("plot", frames)
                cv2.imwrite('results/frame_{}.png'.format(c), frames)
                self.logwriter.write()
                c +=1
                Rstack, Lstack =[], []
            if cv2.waitKey(30) == 27:
                break
        self.capR.release()
        self.capL.release()
        self.logwriter.close()
