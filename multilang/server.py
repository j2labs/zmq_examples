#!/usr/bin/env python

import zmq
import time

ctx = zmq.Context()
s = ctx.socket(zmq.PUB)
s.bind("ipc://hellostream:5678")

while True:
    s.send('helos' + " " + 'Hello!')
    print 'Sending a hello'
    time.sleep(1)
