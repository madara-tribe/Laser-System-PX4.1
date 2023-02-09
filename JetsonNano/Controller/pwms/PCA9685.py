#!/usr/bin/env python

import time
import Adafruit_PCA9685
CYCLE = 50


class ServoController:
    def __init__(self, ):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(CYCLE)
    
    def initialize(self, channel, val):
        self.update_pos(channel, val)
        
    def update_pos(self, channel, angle):
        duty = int(float(angle) * 2.17 + 102)
        self.pwm.set_pwm(channel, 0, duty)
        time.sleep(0.1)
