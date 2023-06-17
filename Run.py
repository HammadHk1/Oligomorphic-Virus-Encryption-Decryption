import Ecryption  #Importing my Encryption class
import Decryption #Importing my Decryption class
import Key        #Importing my Key class  

# Using key class to make key and get key
key = Key.Key()

key.MakeKey()
key.Write_in()

Fernet_key = key.GetKey()

# Checking if the encryption has been done already or not
f = open("hello_world.py", "r")
if (f.read() == 'print("Hello World")'):
# Encrypting the file for the first time
    Enc = Ecryption.Encryption()
    Enc.Make_Encryptor(Fernet_key)
    encryptor = Enc.Open_Encryptor_File(Fernet_key)
    Enc.Encrypt_File(encryptor)
print("=======================================")
# Data in file before decryption
print("Data in File before decryption")
f = open("hello_world.py", "r")
print(f.read())

# Decrypting the file
Dec = Decryption.Decryption()
k = Dec.OP_dec()
n1 = Dec.Open_Decryptor_File(k)
Dec.Decrypt_File(n1)
print("=======================================")
# RUnning the code after decryption
print("Running the code after decryption")
exec(open("./hello_world.py").read())
print("=======================================")

# Encrypting the file
Enc = Ecryption.Encryption()
Enc.Make_Encryptor(Fernet_key)
encryptor = Enc.Open_Encryptor_File(Fernet_key)
Enc.Encrypt_File(encryptor)

print("Data in File After Encryption")
f = open("hello_world.py", "r")
print(f.read())

