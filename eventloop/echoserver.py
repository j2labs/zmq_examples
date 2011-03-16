#!/usr/bin/env python

import zmq
import json
from zmq.eventloop import ioloop, zmqstream
loop = ioloop.IOLoop.instance()

ctx = zmq.Context()
s = ctx.socket(zmq.REP)
s.bind('ipc://127.0.0.1:5678')
stream = zmqstream.ZMQStream(s, loop)

def echo(msg):
    data = json.loads(msg[0])
    print data
    stream.send_multipart(msg)

stream.on_recv(echo)

loop.start()
