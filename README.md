# Oligomorphic-Virus-Encryption-Decryption

## Introduction
We implemented the oligomorphic virus technique. In an Oligomorphic virus, a few decryptors are generated and a random decryptor is chosen. We wrote a basic hello world program in python and ,using the Fernet module of python, implemented the concepts of encryption and decryption to achieve the desired result. Following figure shows the basic flow of an oligomorphic virus.
![image](https://github.com/HammadHk1/Oligomorphic-Virus-Encryption-Decryption/assets/117303560/0a953aca-5536-496e-a39f-acdc245290ba)

## Implementation:
We have made multiple files and separated the classes of encryption, decryption and keys. The main code is implemented in the Run.py file.
### Encryption:
In this encryption file, firstly, we stored our key in keylog.key through which we are going to encrypt a file.
After this, we open our file using rb then the key which was generated is assigned to a variable. After this,  we call the encrypt function through that key to encrypt that file. Then we write this to our original file.
### Decryption:
In this,  we move to keylog.key which contains the key which can be used for decryption. We get our key in OP_Dec. We Open our file and read the file and decrypt the file using the key and then we write back to file the decrypted message.
### Key: 
Here we are using <b>Cryptography.fernet</b> key to generate our 5 keys which is stored to a file here we return a key which is randomly picked up and send this for encryption and decryption
### Flow of the code:
- After importing the 3 classes of encryption,decryption and keys, we’ll generate a random key from the list of already defined keys.
- We’ll check if the program is already encrypted or not. If not, we’ll encrypt it as follows,
- After this, we’ll decrypt the program and execute it.
- Then we’ll re-encrypt the program using the same commands as above..
## Flow Diagram:
![image](https://github.com/HammadHk1/Oligomorphic-Virus-Encryption-Decryption/assets/117303560/599d2b26-e429-4cd7-bbfa-85468720ef4a)
## Commands to run the Program
Download this Directory open the code in VS code. Run Run.py file to execute the code.
```
python Run.py

```

