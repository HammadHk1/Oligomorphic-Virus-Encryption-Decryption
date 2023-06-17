from fileinput import filename
from cryptography.fernet import Fernet
import random as rand
#####################################################
# class for making keys and storing the further use
class Key():
    
    def __init__(self):
        self.flag = True
        self.key_list = []
        # Binary File to store the values of Key in it
        self.filenames = ['Encrpytor1.key','Encrpytor2.key','Encrpytor3.key','Encrpytor4.key','Encrpytor5.key']
     
    def Write_in(self):
        #Moving Keys to Encryptor File
        for i in range(0,5):
            with open(self.filenames[i],'wb') as encrypt_key:
                encrypt_key.write(self.key_list[i])
        
    def MakeKey(self):
        #Creating list of keys
        for i in range(0,5):
            #Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key
            key = Fernet.generate_key()
            self.key_list.append(key)   
        #Printing the Different Keys Generated in the list
        print(" Keys Generated are :: \n",self.key_list)    
    
    def GetKey(self):
        #Getting Random Key from the Key_list to use for Encryption
        num = rand.randint(0,4)
        with open(self.filenames[num],'rb') as KF:
            k = KF.read()
        return k
        
        
            
            
        
                
        
            
        
    