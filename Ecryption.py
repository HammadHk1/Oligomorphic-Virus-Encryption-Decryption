from fileinput import filename
from cryptography.fernet import Fernet
#####################################################
class Encryption():
    def __init__(self):
        #Making Key log to maintain which key was used to encypt the Data...
        self.filename = "Keylog.key"
    
    def Make_Encryptor(self,Fernet_Key):
        #Opening the file to write the Encrypted Key in it
        with open(self.filename,'wb') as encrypt_key:
            encrypt_key.write(Fernet_Key) 
    
    def Open_Encryptor_File(self,Fernet_Key):
        #Opening file for reading which is to be Encrypted..
        with open('hello_world.py','rb') as file:
            org = file.read()
        # key generated is assigned to a variable for usage..     
        f = Fernet(Fernet_Key)
        encrypt = f.encrypt(org)  
        return encrypt
                 
    def Encrypt_File(self,encrypt):
        #Last thing to Encrypt the file using Encrypt used in previous func...
        with open('hello_world.py','wb') as encrypted_file:
            encrypted_file.write(encrypt) 
        
    