import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import base64

def rsakeys():  
     length=1024  
     privatekey = RSA.generate(length, Random.new().read)  
     publickey = privatekey.publickey()  
     return privatekey, publickey

def encrypt(rsa_publickey,plain_text):
     cipher_text=rsa_publickey.encrypt(plain_text,32)[0]
     b64cipher=base64.b64encode(cipher_text)
     return b64cipher

def decrypt(rsa_privatekey,b64cipher):
     decoded_ciphertext = base64.b64decode(b64cipher)
     plaintext = rsa_privatekey.decrypt(decoded_ciphertext)
     return plaintext

privatekey,publickey=rsakeys() #generating keys
text=b"Test Datong Token 2019-06-10" #Text to encrypt
ct=encrypt(publickey,text)
print(ct)
print(decrypt(privatekey, ct)) #decryption

