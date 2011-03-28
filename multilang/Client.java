import org.zeromq.ZMQ;

public class Client {

	public static void main(String args[]) {
		ZMQ.Context ctx = ZMQ.context(1);
		ZMQ.Socket s = ctx.socket(ZMQ.PUB);
		s.bind("ipc://hellostream:5678");
        //s.subscribe("".getBytes());
        //byte[] subStr = "hellos".getBytes();
        
        //System.out.println("SIZE: " + subStr.length);
        //s.subscribe(subStr);
        
		while(1 > 0) {
			byte[] data = s.recv(0);
            System.out.println("Received: " + data);
		}
	}
}
