#DAWN Simple Binary Encryption System
#Version 0.1
#Made by DAWN/ペンギン
#Last Updated: 04-06-2023

def switch(data, key, level):


    def isPrime(num):
        for i in range(2, num):
            if i % num == 0:
                return False
        return True
    

    def binswap(k):
        r = ''
        l = list(k)
        for i in range(0, len(l)-1, 2):
            l[i+1], l[i] = l[i],l[i+1]
        for i in l:
            r+=i
        return r


    sData = ''
    key = binswap(key)


    match level:
        case 0:
            num = 0
            for i in data:
                if key[num] == '1':
                    sData+=str(int(not int(i)))
                else: 
                    sData+=i
                num+=1
                if num == len(key)-1: num = 0
        case 1:
            num = 0
            for i in range(len(data)):
                if i % 2 == 0 and key[num] == '0':
                    sData+=str(int(not int(data[i])))
                else:
                    sData+=data[i]
                num+=1
                if num == len(key)-1: num = 0
        case 2: 
            num = 0
            for i in range(len(data)):
                if isPrime(i) and key[num] == '0':
                    sData+=str(int(not int(data[i])))
                else:
                    sData+=data[i]
                num+=1
                if num == len(key)-1: num = 0
        case 3:
            num = 0
            for i in data:
                sData+=str(int(key[num]) ^  int(i))
                num+=1
                if num == len(key)-1: num = 0
    
    return sData
