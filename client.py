from threading import Thread
import socket

class client(Thread):
    def __init__(self,ip,port,buffer_size,message,ref):
        Thread.__init__(self)
        self.ip=ip
        self.port=port
        self.buffer_size=buffer_size
        self.message=message
        self.ref=ref
    
    def run(self):
        print('client')
        tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        tcpClient.connect((self.ip, self.port))

        while self.message != 'exit':
            print(self.ref)
            tcpClient.send(self.message)     
            data = tcpClient.recv(self.buffer_size)
            print " Client2 received data:", data
            self.message = raw_input("tcpClientA: Enter message to continue/ Enter exit:")
        
        tcpClient.close()
ip='0.0.0.0'
port=5004
message=raw_input('Enter message A')
th1=client(ip,port,20,message,'A')
message=raw_input('Enter message B')
th2=client(ip,port,20,message,'B')

th1.start()
th2.start()
