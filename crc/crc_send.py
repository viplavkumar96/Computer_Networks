def xor(a,b):
        res = []
        for i in range(1,len(b)):
                if(a[i]==b[i]):
                        res.append('0')
                else:
                        res.append('1')
        return ''.join(res)

def find_rem(msg,div):
        l = len(div)
        tmp = msg[0:l]
        while l<len(msg):
                if tmp[0] =='1':
                        tmp = xor(div,tmp)+msg[l]
                else:
                        tmp = xor('0'*l,tmp)+msg[l]
                l +=1
        if tmp[0] == '1':
                tmp = xor(div, tmp)
        else:
                tmp = xor('0'*l, tmp)
        return tmp

inp_msg = raw_input("Enter data\n")
key = '1001'
print "Codeword is:\n",inp_msg+find_rem(inp_msg,key)

