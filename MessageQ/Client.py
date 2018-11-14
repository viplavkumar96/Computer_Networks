import time

print "enter file name to be fetched"
req_file = raw_input().strip()

req = open("req.fifo","w")

req.write(req_file)
req.close()
time.sleep(10)

res = open("res.fifo","r")

print res.read()
