#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
import math
import tf
import geometry_msgs.msg
import os

if __name__ == '__main__':
    rospy.init_node('tf_listener')

    listener = tf.TransformListener()
	
    rate = rospy.Rate(10.0)
    note = open('/home/s/catkin_ws/src/learning_tf/scripts/trajactory1.txt',mode='a')
    print('ord')
    trans=0
    while not rospy.is_shutdown():
        try:
	
	    trans_last = trans
            (trans,orien) = listener.lookupTransform('/map', '/base_link', rospy.Time(0))
            note = open('/home/s/catkin_ws/src/learning_tf/scripts/trajactory1.txt',mode='a')
            if(trans_last != trans):
            	note.write('{} {} {} {} {} {} {} {}\n'.format(rospy.get_time(),trans[0],trans[1],trans[2],orien[0],orien[1],orien[2],orien[3]))
            note.close()
	    print('write one line')
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
		



