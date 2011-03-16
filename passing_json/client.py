#!/usr/bin/env python

import zmq
import json

ctx = zmq.Context()
s = ctx.socket(zmq.PULL)
s.connect("ipc://*:5678")

while True:
    msg = s.recv()
    ds = json.loads(msg)
    print '%s :: %s' % (ds['code'], ds['text'])
