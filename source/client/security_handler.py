import rsa

def generate_new_keys():
    publicKey, privateKey = rsa.newkeys(1024)
    return [publicKey, privateKey]