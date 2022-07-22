# Source of this file: https://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

bs = AES.block_size
iv = ""
key = hashlib.sha256("This is the AES key".encode()).digest()

def create_random_iv():
    return Random.new().read(AES.block_size)

def set_iv(value):
    global iv
    iv = value

def encrypt(raw):
    raw = _pad(raw)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode())).decode().replace('/', '+')

def _pad(s):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def encryptAll(array):
    encrypted_array = []
    for plain in array:
        encrypted_array.append(encrypt(plain))
    return encrypted_array

def decrypt(enc):
    enc = base64.b64decode(enc)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return _unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

def _unpad(s):
    return s[:-ord(s[len(s)-1:])]