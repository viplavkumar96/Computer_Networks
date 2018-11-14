from crc_send import xor,find_rem

msg = raw_input("Enter message recv\n")

#div = raw_input()

if find_rem(msg,'1001')=='000':
    print "Valid data"
else:
    print "Invalid"
