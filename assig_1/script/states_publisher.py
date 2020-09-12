#!/usr/bin/env python
# Created by Mostafa Osama Ahmed
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header , String


def motion():
	pub = rospy.Publisher('joint_states', JointState, queue_size=10)
	rospy.init_node('joint_state_publisher')
	rate = rospy.Rate(150)
	robot = JointState()
	robot.position = [-0.75,1.5,1.5,-1.5,-1.5]
	x = -0.01
	y =  0.01
	h = 0.005
	a = 0

	while not rospy.is_shutdown():
		robot.header = Header()
		robot.header.stamp = rospy.Time.now()
		robot.name = ['base_to_head', 'base_to_right_arm', 'right_arm_to_right_elbow', 'base_to_left_arm', 'left_arm_to_left_elbow']
		# head
		robot.position[0] += h
		# right_arm
		robot.position[1] += x 
		robot.position[2] += x
		# left_arm
		robot.position[3] += y
		robot.position[4] += y

		robot.velocity = []
		robot.effort = []
		rospy.loginfo(robot)
		pub.publish(robot)
		rate.sleep()
		# robot joints speed 
		if robot.position[1] == -1.5000000000000022:
			x = 0.01 
			y = -0.01
			h = -0.005
		elif robot.position[1] == 0.9999999999999997:
			x = 0.01 
			y = -0.01
			h = -0.005
			a += 1
		elif robot.position[3] == -1.5:
			x = -0.01 
			y = 0.01
			h = 0.005
		elif robot.position[3] == 1.5:
			x = -0.01 
			y = 0.01
			h = 0.005
		elif a == 4:
		 	break
				

if __name__ == '__main__':
	try:
		motion()
	except rospy.ROSInterruptException:
		pass

# N.B:
# this could run in the terminal to publish specific joints with its values
# rostopic pub /joint_states sensor_ms/JointState '{header: auto, name: ['base_to_head', 'base_to_right_arm', 'right_arm_to_right_elbow', 'base_to_left_arm', 'left_arm_to_left_elbow'], position: [0,1,1,1,1], velocity: [], effort: []}' 