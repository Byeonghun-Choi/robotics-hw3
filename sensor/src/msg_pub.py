#!/usr/bin/env python
import rospy
from common_msgs.msg import Msg
from common_msgs.srv import Srv, SrvRequest


rospy.init_node('msg_pub', anonymous=True)
requester = rospy.ServiceProxy('srv_requester', Srv)
count = 0
msg = Msg()

pub = rospy.Publisher("DateTime_msg", Msg, queue_size = 1)
rate = rospy.Rate(1)
msg.number.data = 0
msg.rotation.orientation.x = 0.0
msg.rotation.orientation.y = 0.0
msg.rotation.orientation.z = 0.0
msg.rotation.position.x = 0.0
msg.rotation.position.y = 0.0
msg.rotation.position.z = 0.0

while not rospy.is_shutdown():
    count += 1
    msg.number.data += 1
    msg.rotation.orientation.x += 1
    msg.rotation.orientation.y += 1
    msg.rotation.orientation.z += 1
    msg.rotation.orientation.w += 1
    msg.rotation.position.x += 1
    msg.rotation.position.y += 2
    msg.rotation.position.z += 3
    pub.publish(msg)
    if count == 10:
        req = SrvRequest(type1 = True, type2 = False)
        res = requester(req)
        print "Requested data : ", req.type1, req.type2
        print "Responsed data : ", res.result
    elif count == 20:
        req = SrvRequest(type1 = True, type2 = True)
        res = requester(req)
        print "Requested data : ", req.type1, req.type2
        print "Responsed data : ", res.result
        count = 0
        
    print(msg.number)
    print(msg.rotation)
    rate.sleep()



    
    
