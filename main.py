import argparse
import yaml
from software.dual_camera import DualCamera
        
def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dual', action='store_true', help='use 2 CSI cameras')
    parser.add_argument('--plot', action='store_true', help='just plot and not TCP socket trasmission to pyside')
    parser.add_argument('--frame_interval', type=int, default=50, help='camera interval to reduce burden')
    parser.add_argument('--onnx_path', type=str, default='yolov7Tiny_640_640.onnx', help='image path')
    parser.add_argument('--cpu', type=str, default='True', help='if cpu is None, use CUDA')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='conf threshold for NMS or postprocess')
    parser.add_argument('--max_disparity', type=int, default=500, help='max disparity')
    parser.add_argument('--min_disparity', type=int, default=40, help='max disparity')
    parser.add_argument('--hyp', type=str, default='utils/hyp.csi.imx219.yaml', help='CSI IMX219 hyperparameters path')
    opt = parser.parse_args()
    return opt
 
    
def main(opt, hyp):
    DualCamera(opt, hyp)
        
if __name__ == '__main__':
    opt = get_parser()
    # load hyps dict
    with open(opt.hyp, errors='ignore') as f:
        hyp = yaml.safe_load(f)
    main(opt, hyp)

