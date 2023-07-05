======================================
Binary Simple Encryption System (bses)
======================================

A simple binary encryption system made for jade-switch

Introduction
------------------

bses is a simple algorithm written using Python. This module contains a single function switch() which has three parameters. Using this function, you can encrypt (switch) a binary string using another binary string. The encryption system is different for each levels. Currently, three levels are specified which can be passed as an arugement in the function call. bses does not require any extra dependencies and is easy to use. 

Sample Usage
-----------------

To start encrypting binary data, call the switch() function after importing the module to youe program. 

**switch(data, key, level)**
The function takes three parameters. *data* and *key* has to be string and *level* has to be int. 

For example:

``print(switch('100101010', '1010', 0))``

The above code returns '110111000' as output. 

Note that both the return value has the same length as the original data. 

Support
-----------------

Discussions Forum: `GitHub Discussions <https://github.com/flamboyantpenguin/>`_

Feedback: `Feedback Form <https://forms.gle/be12vqFPKoMSpyWs5/>`_

  Version 0.1

  Last Updated: 04-06-2023

  Made by DAWN/ペンギン

  .. image:: https://github.com/flamboyantpenguin/jade-switch/assets/49310641/b28f6250-49ef-49c1-a6b0-79ddf2c00acb
