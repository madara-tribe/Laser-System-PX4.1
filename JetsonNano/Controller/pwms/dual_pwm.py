#!/usr/bin/env python

import Jetson.GPIO as GPIO
import time
import threading
import sys, os
from utils import Xangle2duty, Yangle2duty

OUTPUT_PIN1 = 33 
OUTPUT_PIN2 = 32
CYCLE = 50
t=2

tmpdir="/tmp/tmp_2s487t8"

def Xget():
    Xfr = open(os.path.join(tmpdir, "X.txt"), 'r', encoding='utf-8')
    wdc = float(Xfr.read().replace(',', ''))
    return wdc
    
def Yget():
    Yfr = open(os.path.join(tmpdir, "Y.txt"), 'r', encoding='utf-8')
    hdc = float(Yfr.read().replace(',', ''))
    return hdc

def setup_device():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(OUTPUT_PIN1, GPIO.OUT, initial=GPIO.HIGH)
    pw = GPIO.PWM(OUTPUT_PIN1, CYCLE)

    GPIO.setup(OUTPUT_PIN2, GPIO.OUT, initial=GPIO.HIGH)
    ph = GPIO.PWM(OUTPUT_PIN2, CYCLE)
    return pw, ph

def pw_loop(pw):
    while flag:
        wdc = Xget()
        dc1 = wdc #Angle2Duty(580)
        pw.start(dc1)
        print("width dc {}".format(dc1))
        time.sleep(t)

def ph_loop(ph):
    while flag:
        hdc = Yget()
        dc1 = hdc #Angle2Duty(120)
        ph.start(dc1)
        print("ph height {}".format(dc1))
        time.sleep(t)

if __name__ == '__main__':
    flag = True
    stime = time.time()
    pw, ph = setup_device()
    th1 = threading.Thread(target=pw_loop, args=(pw,))
    th1.start()
    th2 = threading.Thread(target=ph_loop, args=(ph,))
    th2.start()
    while True:
        now = time.time() -stime
        if now==10:
            flag =False
            th1.join()
            th2.join()
            pw.stop()
            ph.stop()
            GPIO.cleanup()
            sys.exit(1)
