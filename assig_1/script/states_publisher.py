import sys
import geometry_msgs.msg
import rospy
from geometry_msgs.msg import Twist,Pose,PoseStamped,PoseArray,Path
from sensor_msgs.msg import jointstate


def motion():
    pub = rospy.Publisher('/joint_states', sensor_msgs.msg, queue_size=10)
    rospy.init_node('motion', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        motion()
    except rospy.ROSInterruptException:
        pass