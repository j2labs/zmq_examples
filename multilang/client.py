#!/usr/bin/env python

import zmq

ctx = zmq.Context()
s = ctx.socket(zmq.SUB)
s.connect("ipc://hellostream:5678")
s.setsockopt(zmq.SUBSCRIBE, 'hellos')

while True:
    msg = s.recv()
    print 'Received: ', msg
