#!/usr/bin/env python

import roslib
import rospy
import rosnode

from std_msgs.msg import String

def pubNodeInfos():
  # TODO: create a rospy.Publisher node
  pub = rospy.Publisher('pubNodeInfo', String, queue_size=1)

  # TODO: initialize the node with rospy.init_node
  rospy.init_node('talker', anonymous=True)
  
  # iteration while running
  while not rospy.is_shutdown():
    nodeString = ""
    
    # TODO: use rosnode.get_node_names to find the names of running nodes
    nodes = rosnode.get_node_names()
    # TODO: concatenate the names adding them to the nodeString   
    for node in nodes
      nodestring += node + " "
    # publishes the concatenated string  
    pub.publish(nodeString)
    rospy.sleep(2)

if __name__ == '__main__':
  try:  
    pubNodeInfos()
  except rospy.ROSInterruptException:
    print "node interrupted"
