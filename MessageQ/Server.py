import time
import os

#req = open("req.fifo","r")
res = open("res.fifo","w")
print "Server Listening"
time.sleep(10)
req = open("req.fifo","r")
req_file = req.read()
print "Requested file is",req_file
try:
        result = open(req_file,"r")
        res.write(result.read())
        print "File %s is sent"%(req_file)
except IOError:
        print "File not found"
