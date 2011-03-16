#!/usr/bin/env python

import zmq
import time

ctx = zmq.Context()

# one socket
s1 = ctx.socket(zmq.PUB)
s1.bind("tcp://127.0.0.1:5566")

# another
s2 = ctx.socket(zmq.PUB)
s2.bind("ipc://*:5567")

while True:
    print 'Camera 1?'
    s1.send("Camera 1")
    time.sleep(1)
    print 'Camera 2?'
    s2.send("Camera 2")
    time.sleep(1)
