#!/usr/bin/env python3

import rospy
import sys
import numpy as np

def dual_cam(set_velocity):
    for _ in range(50):
        linear_vel = float(np.random.rand())
        angular_vel = float(np.random.rand())
        response = set_velocity(linear_vel, angular_vel)
        if response.success:
            rospy.loginfo('set [%f, %f] success' % (linear_vel, angular_vel))
        else:
            rospy.logerr('set [%f, %f] failed' % (linear_vel, angular_vel))

#if __name__ == '__main__':
#    dual_cam()
