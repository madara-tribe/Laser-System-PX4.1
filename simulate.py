import argparse
import time
from simulater.movie_inference import VideoInference


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--onnx_path', type=str, default='simulater/data/yolov7Tiny_640_640.onnx', help='image path')
    parser.add_argument('--cpu', type=str, default='True', help='if cpu is None, use CUDA')
    parser.add_argument('--per_frames', type=int, default=5, help='num frames to predict at each thread for reducing device burden')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='conf threshold for NMS or postprocess')
    parser.add_argument('--max_disparity', type=int, default=240, help='max disparity')
    parser.add_argument('--min_disparity', type=int, default=15, help='max disparity')
    parser.add_argument('--rvid_path', type=str, default='simulater/data/right.mp4', help='right video path')
    parser.add_argument('--lvid_path', type=str, default='simulater/data/left.mp4', help='left video path')
    parser.add_argument('--vid_size', type=int, default=250, help='Display video size')
    opt = parser.parse_args()
    return opt
    
    
if __name__ == '__main__':
    opt = get_parser()
    vid_inference = VideoInference(opt)
    vid_inference.inference()
