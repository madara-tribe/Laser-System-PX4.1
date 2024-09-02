#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from ros_start.srv import SetVelocity, SetVelocityResponse

def velocity_handler(req):
    rep_x = req.x
    rep_y = req.y
    print(rep_x, rep_y)
    is_set_success = True
    return SetVelocityResponse(success=is_set_success)

if __name__ == '__main__':
    rospy.init_node('velocity_server')
    service_server = rospy.Service('set_velocity', SetVelocity, velocity_handler)
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    rospy.spin()
