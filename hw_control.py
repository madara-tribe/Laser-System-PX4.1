import sys, os
import argparse
import yaml
from JetsonNano.main import hw_main

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--plot', action='store_true', help='plot 2 CSI camera frames')
    parser.add_argument('--mov', action='store_true', help='save 2 CSI camera frames was movie')
    parser.add_argument('--pwm', action='store_true', help='PWM with CSI camera')
    parser.add_argument('--hyp', type=str, default='JetsonNano/Controller/utils/hyp.csi.imx219.yaml', help='CSI IMX219 hyperparameters path')
    parser.add_argument('--cpu', type=str, default='True', help='if cpu is None, use CUDA')
    parser.add_argument('--onnx_path', type=str, default='./JetsonNano/Controller/utils/yolov7Tiny_640_640.onnx', help='Onnx model path for hardware')
    parser.add_argument('--per_frames', type=int, default=3,  help='num frames to predict at each thread for reducing device burden')
    parser.add_argument('--conf_thres', type=int, default=0.25, help='conf threshold for NMS or postprocess')
    parser.add_argument('--min_disp', type=int, default=240, help='max disparity')
    parser.add_argument('--max_disp', type=int, default=15, help='max disparity')
    opt = parser.parse_args()
    return opt
    
    
if __name__ == '__main__':
    opt = get_parser()
    hw_main(opt)
