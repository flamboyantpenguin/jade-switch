# jade-switch

A simple file encryption system based on binary switching. Switch is the default algorithm for Jade which encrypts file using binary switching. This method unlike Delta, encrypts a file without consuming extra space. Switch currently supports 3 levels of encryption. The program is written in a class structure to make it easy to intergrate Switch with other programs. Switch is available on Jade Console 1.0 which will be launched soon.

## Sample Usage

To encrypt a file, first a tilda object with required flags must be declared. The following code declares a tilda object 'encrypt' with zero flags.

`encrypt = tilda()`

An existing file can be encrypted as .fje format by using the tilda.eFile() method.

`encrypt.eFile('Hello.txt', 'thisisapassword123', '2')`

A file named Hello.fje will be created with the given password and level[^0].

    Warning: Passwords must contain more than one character as there should be atleast 2 characters in the passkey for bses algortithm to function properly. Passwords should contain atleast 8 letters for recommended security.

The following code decrypts the archive.

`encrypt.dFile('Hello.fje', 'thisisapassword123')`

The file will be decrypted and saved automatically to the working directory. Note that the level is is not specified in the function call as the level is dectected automatically. Err:2 will be returned in case of error.

For more info on tilda class, refer to tilda documentation.

Powered by

![DAWN](https://github.com/flamboyantpenguin/jade-switch/assets/49310641/b28f6250-49ef-49c1-a6b0-79ddf2c00acb)

[^0]: To learn more about levels, refer bses documentation.  
