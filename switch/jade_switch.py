#Jade Switch 1.0 Pre-Alpha
#Made by DAWN/ペンギン
#Last Updated: 03-06-2023


import string
import ses_ph03 as ses
import bses_ph03 as bses
from os import path
from random import choices
from time import time, localtime
from multiprocessing import SimpleQueue


class tilda:

    version = 'jade_switch_1.0'
    errorCode = {1.1:'Err:1.1 Data File Not Found', 1.2: 'Err:1.2 Key File Not Found', 2:'Err:2 Decrypt Key Mismatch'}

    def __init__(self, flags=()):
        self.flags = flags
        self.vkey = self.generateKey(6)
        self.status = 'Empty sfes object'
        self.progress = SimpleQueue()


    def generateKey(self, n):
        if 'jade_includePunctuation' in self.flags:
            l = choices(string.ascii_letters+string.digits+string.punctuation, k=n)
        else:
            l = choices(string.ascii_letters+string.digits, k=n)
        r = ''
        for i in l: r+=i
        return r
    

    def __encode(self, data):
        rData = []
        for i in data:
                n = k = 0
                for j in reversed(i):
                    n+=int(j)*(2**k)
                    k+=1
                rData.append(n)
        return bytes(rData)


    def __decode(self, data):
        rData = []
        for i in data:
            b = bin(i)[2:]
            if len(b)!= 8:
                b='0'*(8-len(b))+b
            rData.append(b)
        return rData
    
    
    def eFile(self, file, key, level):

        
        def encrypt(d):
            sdata = []
            for i in d:
                sdata.append(bses.switch(i, key, self.level))
            return sdata
        
        #Preparing Encryption
        self.progress.put('Preaparing|1')
        etime = time()
        self.fname = file
        self.level = level
        self.header = '<NaAlSi2O6_Tilda_2.2.0>\n<{}_!{}_{}>\n'.format(file, self.vkey, bses.switch('1010100010010010', key, self.level))

        #Loading Data
        self.progress.put('Loading Data|2')
        with open(self.fname, 'rb') as f:
            content = self.__decode(f.read())
        
        #Encrypting Data
        self.progress.put('Encrypting|33')
        edata = encrypt(content)

        #Creating Archive
        self.progress.put('Creating Archive|66')
        t  = self.fname.split('.')
        self.name = t[0]+'.fje'
        with open(self.name, 'wb') as archive:
            archive.write(bytes(self.header, 'UTF-8'))
            archive.write(self.__encode(edata))
        
        #Creating Recovery
        if 'jade_cRecovery' in self.flags:
            self.createRecovery(key)

        self.status = 'Encrypted Archive'
        self.progress.put('Done|100')
        self.etime = int(etime-time())
        return 0
    

    def dFile(self, file, key):
        

        def decrypt(d):
            sdata = []
            for i in d:
                sdata.append(bses.switch(i, key, self.level))
            return sdata
        

        def decodeHeader(header):
            header = header.decode('UTF-8')
            header = header.split('\n')
            header = header[1].split('_')
            header[0] = header[0].removeprefix('<')
            if len(header) == 3: header[2] = header[2].removesuffix('>')
            
            #Checking Level
            ckey = header[2]
            for i in range(4):
                 if bses.switch(ckey, key, i) == '#(Serendipity)':
                      header.append('Level {}'.format(i))
                      self.level = i
                      break
                 else:
                    self.progress.put('Error|2')
                    return 'Error'
            return header
        

        #Preparing Decryption
        self.progress.put('Preparing|1')
        dtime = time()
        self.name= file
        if path.exists(file) == False:
            self.progress.put('Error|1.1')
            return 1.1

        #Loading Data
        self.progress.put('Loading Data|8')
        with open(file, 'rb') as archive: 
            self.file_info = decodeHeader(archive.read(57))
            if self.file_info == 'Error': return 2
            data = self.__decode(archive.read())

        #Decrypting Data
        self.progress.put('Decrypting|33')
        content = decrypt(data)

        #Creating File
        self.progress.put('Creating file|66')
        self.fname = self.file_info[0]
        with open(self.fname, 'wb') as file:
            file.write(self.__encode(content))

        self.status = 'Decrypted Archive'
        self.progress.put('Done|100')
        self.dtime = int(dtime-time())
        return 0
    

    def getTime(self):
        t = list(localtime())
        r = ''
        for i in range(len(t)-2):
            r+=str(t[i])
        return r
    

    def createRecovery(self, key):
    

        def encryptKey(key):
            if len(key) < 10: r = '0'+str(len(key))
            else: r = str(len(key))
            c = self.generateKey(40)
            i, n = 0,0
            while n < len(key) and i < len(c):
                if i%2 == 0:
                    r+=key[n]
                    n+=1
                else:
                    r+=c[i]
                i+=1
            r+=c[i:]
            return r


        key = ses.encrypt(key,'NaAlSi206')
        rname = 'jaderecovery_'+self.getTime()+'.jrf'
        header = '<NaAlSi2O6_2.0.1>\n<{}_{}>\n'.format(self.fname, self.vkey)
        content = encryptKey(key)

        with open(rname, 'wb') as archive:
            archive.write(bytes(header, 'UTF-8'))
            archive.write(bytes(ses.encrypt(content, 'NaAlSi2O6'), 'UTF-8'))
        
        return rname
