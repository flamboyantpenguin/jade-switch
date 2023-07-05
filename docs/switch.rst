===========
jade-switch
===========

A simple file encryption system used as Default for Jade Advanced Encryption System.

Introduction
------------

Switch is the currently used default encryption for Jade. This module comes with a class ``tilda``. A class based model has been chosen for easier integration with other applications. Apart from methods for basic encryption/decryption, there are methods for generating keys, useful variables like version_info, filename etc. For encrypting a file, a tilda object should be declared with the requiredflags [#]_. For basic encryption and decryption ``tilda.eFile(self, file, key, level)`` and ``tilda.dFile(self, file, key)`` methods are used. 

Features
--------

- Easy to use
- Encryption/Decryption Status [#]_ 
- class based structure for easy integration 


.. rubric:: Footnotes
.. [#] flags
.. [#] Encryption status using Queue
