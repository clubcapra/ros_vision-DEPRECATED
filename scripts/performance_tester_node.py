#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image

diffs = []
def callback(msg):
    diff = (rospy.get_time() - msg.header.stamp.to_sec()) * 1000
    diffs.append(diff)
    if len(diffs) > 20:
        del diffs[1]
    print sum(diffs) / len(diffs)



rospy.init_node('performance_tester_node')

rospy.Subscriber("/main/mask/output", Image, callback)

rospy.spin()