from math import *

def isPowerOfTwo(n):
    x = int(log(n, 2))
    return (n - 2**x == 0)

def getBinaryString(n,numbits):
    bs = toBinary(n)
    return bs.rjust(numbits, '0')

def toBinary(n):
    if (n == 0):
        return ''
    else:
        return ( toBinary(n//2) + str(n%2) )
                           
def getSubset(elemList, fmt):
    answer = []
    for i in range(len(fmt)):
        if (fmt[i]=='1'):
            answer.append(elemList[i])
    return answer

def powerset(s):
    binlist = []
    numbits = len(s)
    #print numbits
    for i in range(0, 2**numbits):
        bs = getBinaryString(i, numbits)
        #print (i, bs)
        binlist.append(bs)
    answer=[]
    for fmt in binlist:
        x=getSubset(s, fmt)
        #print x
        answer.append(x)
    return answer
    
s =['P', 'Q', 'R', 'S']
ps = powerset(s)
print (ps)
