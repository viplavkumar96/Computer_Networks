import socket
import time

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 5690

server.bind(('',port))
print "Server Listening"
server.listen(5)

while True:
        c, addr = server.accept()
        print "Connection request from", addr
        print "Connected to", addr
        time.sleep(2)
        print c.recv(1024)
        c.send("Thank you for connecting")
        request = c.recv(1024)
        try:
                ToSend = open(request,"r")
        except IOError:
                c.send("File Not Found")
                c.send('')
                continue
        l = ToSend.read()
        while(l):
                c.send(l)
                l = ToSend.read()
        ToSend.close()
