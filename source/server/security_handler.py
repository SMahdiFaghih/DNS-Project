import os
import rsa
import base64

public_key = ""
private_key = ""

path = os.path.join(os.path.dirname(__file__), "key")
if not os.path.exists(path):
    os.mkdir(path)
    (publicKey, privateKey) = rsa.newkeys(1024)
    p = open(path + "/publicKey.pem", 'wb')
    p.write(publicKey.save_pkcs1('PEM'))
    p.close()
    p = open(path + "/privateKey.pem", 'wb')
    p.write(privateKey.save_pkcs1('PEM'))
    p.close()
with open(path + "/publicKey.pem", 'rb') as p:
    public_key = rsa.PublicKey.load_pkcs1(p.read())
with open(path + "/privateKey.pem", 'rb') as p:
    private_key = rsa.PrivateKey.load_pkcs1(p.read())

def encrypt(plain_text):
    ciphertext = rsa.encrypt(plain_text.encode("ascii"), public_key)
    encoded = base64.b64encode(ciphertext)
    return encoded.decode()

def decrypt(cipher_text):
    cipher_text = base64.b64decode(cipher_text)
    return rsa.decrypt(cipher_text, private_key).decode("ascii")