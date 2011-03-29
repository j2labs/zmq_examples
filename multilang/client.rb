#!/usr/bin/env ruby

require 'rubygems'
require 'ffi-rzmq'

ctx = ZMQ::Context.new(1)
s = context.socket(ZMQ::SUB)
s.connect("ipc://hellostream:5678")
s.setsockopt(ZMQ::SUBSCRIBE, "hellos")

while 1 > 0
  reply = requester.recv_string
  puts "Received: #{reply}"
end
