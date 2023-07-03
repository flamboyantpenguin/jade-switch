# jade-switch
A simple file encryption system based on binary switching.  

## Sample Usage
To encrypt a file, first a tilda object with required flags must be declared. The following code declares a tilda object 'encrypt' with zero flags. 

`encrypt = Tilda()`

### tilda.eFile(self, filename, key, [level)
  eFile reads data from the given file and encrypts them as \<filename>.fje format. For example, for a tilda object encrypt, the following code 

  `encrypt.eFile('hello.txt', 'thisisapassword123', 2)`
  
encrypts a file named hello.txt with the given password and level 2[^0] encryption. 








[^0]: To learn more about levels, refer bses documentation.  
