import rsa
import base64

def generate_new_keys():
    publicKey, privateKey = rsa.newkeys(1024)
    return [publicKey, privateKey]

def encrypt(plain_text, public_key):
    ciphertext = rsa.encrypt(plain_text.encode("ascii"), public_key)
    encoded = base64.b64encode(ciphertext)
    return encoded.decode()

def decrypt(cipher_text, private_key):
    cipher_text = base64.b64decode(cipher_text)
    return rsa.decrypt(cipher_text, private_key).decode("ascii")