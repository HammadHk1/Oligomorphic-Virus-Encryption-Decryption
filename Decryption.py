from fileinput import filename
from cryptography.fernet import Fernet
#####################################################

class Decryption():
    def __init__(self):
        # to maintain the Key which is used latest..
        self.filename = "Keylog.Key"
    
    def OP_dec(self):
        #Opening key log to get the key for decryption
        with open(self.filename,'rb') as DK:
            k = DK.read()
        return k
    
    def Open_Decryptor_File(self,Key):
        #opening the file for reading
        f = Fernet(Key)
        with open('hello_world.py', 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        #Decrypting the data from the encrypted key....    
        decrypted = f.decrypt(encrypted)
        return decrypted
    
    def Decrypt_File(self,decrypted):
        #writing in file to get back the encrypted data...
        with open('hello_world.py', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
    
    