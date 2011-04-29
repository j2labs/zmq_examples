#!/usr/bin/env python

import zmq
import time

ctx = zmq.Context()

# one socket
s = ctx.socket(zmq.PUB)
s.bind("tcp://127.0.0.1:5566")

# two topics
topic_1 = "camera_1"
topic_2 = "camera_2"

while True:
    print 'Say something to camera_1'
    s.send("%s Party on, Wayne." % topic_1)
    time.sleep(1)

    print 'Say something to camera_2'
    s.send_multipart([topic_2, "Party on, Garth."])
    time.sleep(1)

    print 'Say something to *thin air*'
    s.send("%s If a tree falls in the woods..." % "nowhere")
    time.sleep(1)
