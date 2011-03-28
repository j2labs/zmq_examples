#include <stdio.h>
#include <zmq.h>

int main() {
    void *ctx = zmq_init (1);
    void *s = zmq_socket (ctx, ZMQ_SUB);
    zmq_setsockopt (s, ZMQ_SUBSCRIBE, "hellos", 0);
    zmq_connect (s, "ipc://hellostream:5678");

    while(1) {
        zmq_msg_t msg;
        zmq_msg_init (&msg);
        zmq_recv (s, &msg, 0);
        printf("Received: %s\n", 
               (char *) zmq_msg_data (&msg));
        zmq_msg_close (&msg);
    }

    return 0;
}

