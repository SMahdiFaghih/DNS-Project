import os
import rsa
import base64
from .names_security_handler import *

path = os.path.join(os.path.dirname(__file__), "Keys")
if not os.path.exists(path):
    os.mkdir(path)  

public_key = ""
private_key = ""

def generate_new_keys(username):
    path = os.path.join(os.path.dirname(__file__) + "/Keys", username)
    if not os.path.exists(path):
        os.mkdir(path)
        (publicKey, privateKey) = rsa.newkeys(1024)
        p = open(path + "/publicKey.pem", 'wb')
        p.write(publicKey.save_pkcs1('PEM'))
        p.close()
        p = open(path + "/privateKey.pem", 'wb')
        p.write(privateKey.save_pkcs1('PEM'))
        p.close()
        p = open(path + "/iv.txt", 'wb')
        p.write(create_random_iv())
        p.close()

def get_keys(username):
    global public_key
    global private_key
    path = os.path.join(os.path.dirname(__file__) + "/Keys", username)
    with open(path + "/publicKey.pem", 'rb') as p:
        public_key = rsa.PublicKey.load_pkcs1(p.read())
    with open(path + "/privateKey.pem", 'rb') as p:
        private_key = rsa.PrivateKey.load_pkcs1(p.read())
    with open(path + "/iv.txt", 'rb') as p:
        set_iv(p.read())

def encrypt(plain_text):
    ciphertext = rsa.encrypt(plain_text.encode("ascii"), public_key)
    encoded = base64.b64encode(ciphertext)
    return encoded.decode()

def decrypt(cipher_text):
    cipher_text = base64.b64decode(cipher_text)
    return rsa.decrypt(cipher_text, private_key).decode("ascii")