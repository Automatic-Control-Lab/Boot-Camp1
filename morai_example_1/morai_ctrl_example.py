#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,os

from morai_msgs.msg import CtrlCmd, MultiEgoSetting
import json
import rospy
import numpy as np


class genCtrlCmd:
    

    def __init__(self):
        
        #publisher        
        self.ctrl_cmd_pub = rospy.Publisher('/ctrl_cmd',CtrlCmd, queue_size=1) ## Vehicle Control        

        self.main()


    def main(self):

        ctrl_msg= CtrlCmd()

        frameRate = 50
        rate = rospy.Rate(frameRate) 

        while not rospy.is_shutdown():

            steering_angle = -36

            ctrl_msg.steering     = np.deg2rad(steering_angle)/gear_ratio

            gear_ratio = 1
            
            ctrl_msg.longlCmdType = 2
            

            if ctrl_msg.longlCmdType  == 1:

                ctrl_msg.accel        = 0
                ctrl_msg.brake        = 0

                ctrl_msg.velocity     = 0
                ctrl_msg.acceleration = 0

            elif ctrl_msg.longlCmdType == 2:

                ctrl_msg.velocity     = 20

                ctrl_msg.accel        = 0
                ctrl_msg.brake        = 0

            elif ctrl_msg.longlCmdType == 3:

                ctrl_msg.acceleration = 0 # NEED TO ADD

                ctrl_msg.accel        = 0
                ctrl_msg.brake        = 0
                ctrl_msg.velocity     = 0

            self.ctrl_cmd_pub.publish(ctrl_msg) ## Vehicl Control 출력

            rate.sleep()


if __name__ == "__main__":

    try:

        rospy.init_node('genCtrlCmd', anonymous=True)
        genCtrlCmd()
        rospy.spin()

    except rospy.ROSInterruptException:
        pass