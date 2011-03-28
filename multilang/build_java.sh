JZMQ_SRC_DIR="$HOME/Src/jzmq/src"
LIBJZMQ_DIR="/opt/local/lib"
javac -cp $JZMQ_SRC_DIR Client.java
echo "java -Djava.library.path=$LIBJZMQ_DIR -classpath$JZMQ_SRC_DIR:. Client"
echo ""
echo "    I haven't gotten the java demo working yet, btw..."
  
