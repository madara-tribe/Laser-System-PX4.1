import rospy
from client import dual_cam
from ros_start.srv import SetVelocity

def main():
    rospy.init_node('velocity_client')
    set_velocity = rospy.ServiceProxy('set_velocity', SetVelocity)
    dual_cam(set_velocity)

if __name__=='__main__':
    main()
