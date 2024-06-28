import argparse
import os
from tkinter import Tk
from multiprocessing import Process, Queue

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--y_defalut', type=int, default=122, help='y default angle')
    parser.add_argument('--x_defalut', type=int, default=153, help='x default angle')
    opt = parser.parse_args()
    return opt


def main(q):

    calibrate = None
    opt = get_parser()
    if calibrate:
        from Hardware.tkinter_pan_tilt import App
        root = Tk()
        root.wm_title('Servo Control')
        app = App(root)
        root.geometry("220x120+0+0")
        root.mainloop()
    else:
        from Hardware.hardware_thread import hw_thread 
        hw_thread(q, opt)

if __name__=='__main__':
    q = Queue()
    p1 = Process(target = main, args=(q,))
    #p2 = Process(target = hardware_threads, args=(q,))
    p1.start()
    #p2.start()
    p1.join()
    # p2.join()
