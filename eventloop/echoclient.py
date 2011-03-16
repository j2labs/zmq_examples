#!/usr/bin/env python

import zmq
import json

ctx = zmq.Context()
s = ctx.socket(zmq.REQ)
s.connect("ipc://127.0.0.1:5678")

x = 0
while x < 5:
    msg = { 'j2': 'was here', 'word': 'up' }
    s.send(json.dumps(msg))
    msg = s.recv()
    print 'MSG: %s' % (msg)
    x += 1
