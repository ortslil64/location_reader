#!/usr/bin/env python
import math
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped 
from geometry_msgs.msg import Pose2D
x = 0.0
y = 0.0
theta = 0.0

def pose_callback(data):
    global x,y,theta
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    theta=math.atan(1-2*((data.pose.pose.orientation.z)**2))
    
   


def get_location():
    
    rospy.init_node('location_reader', anonymous=True)
    rospy.Subscriber("/robot_pose_ekf/odom_combined", PoseWithCovarianceStamped, pose_callback)
    location_pub = rospy.Publisher('/location_or', Pose2D, queue_size=1000)
    rate = rospy.Rate(100) # 10hz
    pos_msg = Pose2D()
    while not rospy.is_shutdown():
        rospy.loginfo(x)
	pos_msg.x=x
	pos_msg.y=y
	pos_msg.theta=theta
        location_pub.publish(pos_msg)
        rate.sleep()

    

if __name__ == '__main__':
    try:
        get_location()
    except rospy.ROSInterruptException:
        pass


 

    