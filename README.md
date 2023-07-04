# jade-switch
A simple file encryption system based on binary switching.  

## Sample Usage
To encrypt a file, first a tilda object with required flags must be declared. The following code declares a tilda object 'encrypt' with zero flags. 

`encrypt = tilda()`

### tilda.eFile(self, file, key, level)
  eFile reads data from the given file and encrypts them as \<filename>.fje format. For example, for a tilda object encrypt, the following code 

  `encrypt.eFile('hello.txt', 'thisisapassword123', 2)`
  
encrypts a file named hello.txt with the given password and level 2[^0] encryption.

Note: Passwords must contain more than one character as there should be atleast 2 characters in the passkey for bses algortithm to function properly. Passwords should contain atleast 8 letters for recommended security. 

### tilda.dFile(self, filename, key)
  eFile reads data from the given file and encrypts them as \<filename>.fje format. For example, for a tilda object encrypt, the following code 

  `encrypt.eFile('hello.txt', 'thisisapassword123')`
  
encrypts a file named hello.txt with the given password and level 2[^0] encryption. 




Powered by

![DAWN](https://github.com/flamboyantpenguin/jade-switch/assets/49310641/b28f6250-49ef-49c1-a6b0-79ddf2c00acb)




[^0]: To learn more about levels, refer bses documentation.  
