#!/usr/bin/env python

import zmq

ctx = zmq.Context()
s = ctx.socket(zmq.SUB)
s.connect("tcp://127.0.0.1:5566")

# subscribe
topic = "camera_1"
s.setsockopt(zmq.SUBSCRIBE, topic)

while True:
    msg = s.recv()
    print msg
