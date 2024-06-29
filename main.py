import argparse
import yaml
from tkinter import Tk
from multiprocessing import Process, Queue


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pwm', action='store_true', help='real action')
    # soft ware
    parser.add_argument('-st', '--software_test', action='store_true', help='software test, inrefence and plot')
    parser.add_argument('--frame_interval', type=int, default=50, help='camera interval to reduce burden')
    parser.add_argument('--onnx_path', type=str, default='yolov7Tiny_640_640.onnx', help='image path')
    parser.add_argument('--cpu', type=str, default='True', help='if cpu is None, use CUDA')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='conf threshold for NMS or postprocess')
    parser.add_argument('--max_disparity', type=int, default=500, help='max disparity')
    parser.add_argument('--min_disparity', type=int, default=40, help='max disparity')
    parser.add_argument('--hyp', type=str, default='setup_utils/csicam/hyp.csi.imx219.yaml', help='CSI IMX219 hyperparameters path')
    # hard ware
    parser.add_argument('-ht', '--hard_test', action='store_true', help='hardware calibrate')
    parser.add_argument('--y_defalut', type=int, default=161, help='y default angle')
    parser.add_argument('--x_defalut', type=int, default=58, help='x default angle')
    opt = parser.parse_args()
    return opt
 
    
def software_threads(q):
    from software.dual_camera import DualCamera
    opt = get_parser()
    # load hyps dict
    with open(opt.hyp, errors='ignore') as f:
        hyp = yaml.safe_load(f)
    DualCamera(q, opt, hyp)

def hardware_threads(q):
    opt = get_parser()
    if opt.hard_test:
        from Hardware.tkinter_pan_tilt import App
        root = Tk()
        root.wm_title('Servo Control')
        app = App(root)
        root.geometry("220x120+0+0")
        root.mainloop()
    elif opt.pwm:
        from Hardware.hardware_thread import hw_thread 
        hw_thread(q, opt)

if __name__ == '__main__':
    opt = get_parser()
    q = Queue()
    if opt.hard_test:
        p2 = Process(target = hardware_threads, args=(q,))
        p2.start()
        p2.join()
    elif opt.software_test:
        p1 = Process(target = software_threads, args=(q,))
        p1.start()
        p1.join()
    elif opt.pwm:
        p1 = Process(target = software_threads, args=(q,))
        p2 = Process(target = hardware_threads, args=(q,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()

