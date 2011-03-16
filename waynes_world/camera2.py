#!/usr/bin/env python

import zmq

ctx = zmq.Context()
s = ctx.socket(zmq.SUB)
s.connect("ipc://*:5567")
s.setsockopt(zmq.SUBSCRIBE, '')

while True:
    msg = s.recv()
    print "MSG 2: ", repr(msg)
