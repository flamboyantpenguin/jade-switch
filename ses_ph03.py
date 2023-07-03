#DAWN Simple Encryption System 3-Phase
#Made by DAWN/ペンギン
#Last Updated: 20-11-2022

def encrypt(data, key):

    def appendChar(c, k):
        c+=k
        if c > 1114111:
            c = c-1114112
        return c

    def binswap(l):
        for i in range(0, len(l)-1, 2):
            l[i+1], l[i] = l[i],l[i+1]
    
    data = [ord(i) for i in data]
    key = [ord(i) for i in key]

    #Phase2
    binswap(key)

    #Phase3
    key.reverse()

    num = 0
    eData = ''
    
    for i in data:
        eData+=chr(appendChar(i, key[num]))
        num+=1
        if num == len(key)-1: num = 0
    
    return eData

def decrypt(data, key):
    
    def reverseChar(c, k):
        c-=k
        if c < 0:
            c = 1114112 - (-c)
        return c

    def binswap(l):
        for i in range(0, len(l)-1, 2):
            l[i+1], l[i] = l[i],l[i+1]
    
    data = [ord(i) for i in data]
    key = [ord(i) for i in key]

    #Phase2
    binswap(key)
    
    #Phase3
    key.reverse()

    num = 0
    dData = ''
    
    for i in data:
        dData+=chr(reverseChar(i, key[num]))
        num+=1
        if num == len(key)-1: num = 0

    return dData
