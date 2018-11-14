import socket
import time

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = socket.gethostname()
port = 5690

client.bind(('',5005))
print "Enter hostname to find the ip address"
hostname = raw_input().strip()

client.sendto(hostname,("127.0.0.1",port))

data,addr =  client.recvfrom(1024)

print hostname,data
