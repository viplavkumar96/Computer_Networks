import socket

import time

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('',5690))

server.listen(5)

while 1:
	c,addr = server.accept()
	print "Request from",addr
	time.sleep(2)
	fl = c.recv(1024)
	try:
		to = open(f1,"r")
	except IOError:
		c.send("File Not Found")
		c.send('')
	l = to.read()
	while l:
		c.send(l)
		l = to.read()
	to.close