import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()

port = 5690

if  client.connect(("127.0.0.1",port))!=None:
        print "Connection refused"
        sys.exit(0)

client.send("Hello Server")

print client.recv(1024)
print "Enter file to be fetched from Server??"
file_req = raw_input().strip()

client.send(file_req)

l = client.recv(1024)
print l
