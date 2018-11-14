def findcode(data):
        r0 = int(data[0])^int(data[1])^int(data[2])
        r1 = int(data[1])^int(data[2])^int(data[3])
        r2 = int(data[0])^int(data[1])^int(data[3])
        return data+str(r2)+str(r1)+str(r0)

def checkcode(code):
        r0 = int(code[0])^int(code[1])^int(code[2])^int(code[len(code)-1])
        r1 = int(code[1])^int(code[2])^int(code[3])^int(code[len(code)-2])
        r2 = int(code[0])^int(code[1])^int(code[3])^int(code[len(code)-3])
        if r0==0 and r1==0 and r2==0:
                print "Received codeword is accepted"
        else:
                print "Error in the received codeword"
                errcode = str(r2)+str(r1)+str(r0)
                if errcode=="001":
                        erri = len(code)-1
                elif errcode=="010":
                        erri = len(code)-2
                elif errcode=="011":
                        erri = 2
                elif errcode=="100":
                        erri = len(code)-3
                elif errcode=="101":
                        erri = 0
                elif errcode=="110":
                        erri = 3
                elif errcode=="111":
                        erri = 1
                temp = []
                for i in code:
                        temp.append(str(i))
                if temp[erri]=='0':
                        temp[erri] = '1'
                else:
                        temp[erri] = '0'
                gen = ''.join(temp)
                print "Corrected code word is :",gen




dataword = raw_input("Enter data word : ")

print findcode(dataword)

codeword = raw_input("Enter received codeword : ")

checkcode(codeword)
