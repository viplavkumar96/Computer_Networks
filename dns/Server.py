import socket
import time

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = socket.gethostname()
port = 5690
dns = dict()
dns = {"localhost":"127.0.0.1","admin":"145.9.76.123","user":"255.55.108.3" }
server.bind(('',port))
print "Server Listening"


while True:
        data, addr = server.recvfrom(1024);
        print "DNS request from ",addr

        if data in dns.keys():
                server.sendto(dns[data],addr)
        else:
                server.sendto("Server doesn't have the required domain address",("127.0.0.1",5005))
                print "Server doesn't have the required domain address"

