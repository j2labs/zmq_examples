# ZeroMQ examples with Python

This project is just a repository for examples for of how to ZeroMQ with Python. These particular examples allow someone to get up and running to test their setup before moving on to coding. 

ZeroMQ setups usually have a few moving parts and it would be a shame for someone to get discouraged by being unsure if they have the code right when it's a setup issue, and versa vice.

# The projects

I recommend trying the examples in the same order I describe them. Each example grows in complexity.

## Wayne's World

Remember the scene where Wayne closes one eye and says, "Camera 1", then opens it and closes the other eye and says, "Camera 2"? That's effectively what's happening here.

Turn on the server and you'll see it print the following:

    $ ./server.py 
    Camera 1?
    Camera 2?
    Camera 1?
    Camera 2?
    
Under the hood, it's actually sending a message down a TCP socket, then an IPC socket and alternating until you hit Ctrl-C. When the server prints "Camera 1?" it is sending the string "Camera 1" to the TCP socket. And, as you might guess, seeing "Camera 2?" means it sent a string to the IPC socket.

We don't have to turn the clients on for the server to send messages. They just don't go anywhere. This example uses a PUB/SUB setup from ZeroMQ. You can use a key to subscribe to particular types of messages if necessary. I don't do that here though.

If we turn on a client `camera1.py`, we see the client start receiving messages. This is close to what we'd expect from a regular socket connection.

    $ ./camera1.py 
    MSG 1:  'Camera 1'
    MSG 1:  'Camera 1'

Same thing for camera2:

    $ ./camera2.py 
    MSG 2:  'Camera 2'
    MSG 2:  'Camera 2'

What do you think happens if we turn on `camera1.py` twice instead? You should try it! 
    
## Passing JSON

This example demonstrates how a pool of workers might be constructed. The PUSH/PULL pattern let's us connect as many clients to the message socket as we need and ZeroMQ will handle the load-balancing for us. It sends message round-robin to each of the connected handlers.

Let's turn the server on.

    $ ./server.py 
    Hello world?

We see that server has sent only one message. A PUSH socket will block until there is at least one client connected.

One we turn on a client, `client.py`, we see the client immediately handle a message. The server then sends a message once a second to the client.

    $ ./client.py 
    200 :: hello world

Disconnect your client and you will see the server block again. Turn on two clients and watch each client take turns receiving a message.

## Wayne's World 2

This example uses a single TCP PUB socket, but uses `camera_1` and `camera_2` as the subscription topic. 

The server sends to `camera_1`, sleeps for a second, sends to `camera_2`, sleeps for a second and then sends a message to `nowhere`. There is no code to handle `nowhere`, so this message just disappears.

The code to send to `camera_1` looks like this:

    s.send("%s Party on, Wayne." % topic_1)

The topic is the first string in the message. This gets interpretted as the topic, so `camera1.py` will pick it up. But you can see how this would be tricky...

The code to send to `camera_2` looks like this:

    s.send_multipart([topic_2, "Party on, Garth."])

The topic is now separate from the message. The receiver can receive this multipart message as a single message, but it will get it each part separately. This is what `camera1.py` does. 

Configuring a subscriber to listen to topics is easy. You call `setsockopt(zmq.SUBSCRIBE, <topic>)` on the socket. That's only part of it though.

A client will receive the topic as part of the message, even though we know they're subscribed. This is because a client can subscribe to multiple topics. ZeroMQ itself will drop any messages that a client hasn't subscribed to and will then say, "here's a message from this `topic`". 

As we saw before, you can simply call `recv()` and get a single line. `camera1.py` prints this, for example.

    camera_1 Party on, Wayne.

Here is what happens when we call `recv()` on a message that was sent as a multipart message, as `camera2.py` does.

    camera2
    Party on, Garth.

Each item is caught separately from a call to `recv()`. It would be more correct to call `recv_multipart`, but that's left as an exercise for you.

## Eventloop

Eventloop leverages some of the work that has been done to put ZeroMQ in Tornado's IOLoop. The work ,`ZMQStream.py`, appears to have been done by Facebook, the same people that open sourced Tornado in the first place. Sweet.

This example builds an echo server by connecting a callback to a ZMQStream, which is running inside the IOLoop. The client does not use the IOLoop. Experienced Tornado hackers will recognize the use of IOStream to hook the socket in.

# What next?

ZeroMQ is a big project. I recommend reading the [ZeroMQ guide](http://zguide.zeromq.org/) first. 

You might also dig two other projects I have:

* [Brubeck](https://github.com/j2labs/brubeck) is an asynchronous message handler optimized for handling [Mongrel2](http://mongrel2.org) messages. It is almost a complete web framework.
* [Dillinger](https://github.com/j2labs/dillinger) is an rough sketch of how one could use Tornado's asynchronous features to wait on ZeroMQ sockets, similar to how it can wait on HTTP requests before responding to a user.
