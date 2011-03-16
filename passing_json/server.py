#!/usr/bin/env python

import zmq
import time
import json

ctx = zmq.Context()

# another
s = ctx.socket(zmq.PUSH)
s.bind("ipc://*:5678")

while True:
    print 'Hello world?'
    msg = {
        'code': 200,
        'text': 'hello world',
    }
    msg_json = json.dumps(msg)
    s.send(msg_json)
    time.sleep(1)
