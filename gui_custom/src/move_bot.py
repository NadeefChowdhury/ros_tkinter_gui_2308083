#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import time
class move_bot:
    def __init__(self) -> None:
        rospy.init_node("mover_node", anonymous=True)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber("/nadeef_command", String, self.callback)
    def callback(self, command):
        rospy.loginfo("Command received: " + command.data)
        global prevTime
        direction = command.data
        
        velocity = Twist()
        def meula():
            while True:
                velocity.angular.z = -5.0
                self.pub.publish(velocity)
                if(time.time()-prevTime >= 1.3):
                    velocity.angular.z = 0.0
                    self.pub.publish(velocity)
                    break
        if direction.lower()=='forward':
            velocity.linear.x = 1.0
            velocity.linear.y = 0.0
            velocity.linear.z = 0.0
        elif direction.lower()=='backward':
            velocity.linear.x = -1.0
            velocity.linear.y = 0.0
            velocity.linear.z = 0.0
        elif direction.lower()=='left':
            velocity.angular.z = 1.0
            velocity.linear.y = 0.0
            velocity.linear.z = 0.0
        elif direction.lower()=='right':
            velocity.angular.z = -1.0
            velocity.linear.y = 0.0
            velocity.linear.z = 0.0
        elif direction.lower()=='stop':
            velocity.linear.x = 0.0
            velocity.linear.y = 0.0
            velocity.linear.z = 0.0
            velocity.angular.z = 0.0
        elif direction.lower()=='meula':
            prevTime = time.time()
            meula()
        else:
            rospy.loginfo("Wrong command")
        try:
            self.pub.publish(velocity)
        except:
            rospy.loginfo("AN ERROR OCCURED")
if __name__=='__main__':
    node = move_bot()
    rospy.spin()