import argparse
import yaml
from software.dual_camera import DualCamera
        
def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dual', action='store_true', help='use 2 CSI cameras')
    parser.add_argument('--plot', action='store_true', help='just plot and not TCP socket trasmission to pyside')
    parser.add_argument('--hyp', type=str, default='csicam_utils/hyp.csi.imx219.yaml', help='CSI IMX219 hyperparameters path')
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

