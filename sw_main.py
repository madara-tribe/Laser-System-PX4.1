import argparse
import yaml
from software.dual_camera import DualCamera
from multiprocessing import Process, Queue


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pwm', action='store_true', help='real action')
    parser.add_argument('-st', '--software_test', action='store_true', help='software test, inrefence and plot')
    parser.add_argument('--frame_interval', type=int, default=50, help='camera interval to reduce burden')
    parser.add_argument('--onnx_path', type=str, default='yolov7Tiny_640_640.onnx', help='image path')
    parser.add_argument('--cpu', type=str, default='True', help='if cpu is None, use CUDA')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='conf threshold for NMS or postprocess')
    parser.add_argument('--max_disparity', type=int, default=500, help='max disparity')
    parser.add_argument('--min_disparity', type=int, default=40, help='max disparity')
    parser.add_argument('--hyp', type=str, default='setup_utils/csicam/hyp.csi.imx219.yaml', help='CSI IMX219 hyperparameters path')
    opt = parser.parse_args()
    return opt
 
    
def software_threads(q):
    opt = get_parser()
    # load hyps dict
    with open(opt.hyp, errors='ignore') as f:
        hyp = yaml.safe_load(f)
    DualCamera(q, opt, hyp)
        
if __name__ == '__main__':
    q = Queue()
    p1 = Process(target = software_threads, args=(q,))
    #p2 = Process(target = hardware_threads, args=(q,))
    p1.start()
    #p2.start()
    p1.join()
    # p2.join()
