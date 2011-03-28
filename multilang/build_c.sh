GCC_OPTS="-I/opt/local/include -L/opt/local/lib"
GCC_FLAGS="-lzmq"
gcc $GCC_OPTS client.c $GCC_FLAGS
