from unicodedata import name


class UI:
    def __init__(self) -> None:
        pass

class User:
    def __init__(self, name, public_key, private_key) -> None:
        self.name = name
        self.public_key = public_key
        self.private_key = private_key
    
    def encrypt(self, input_text):
        pass

    def decrypt(self, input_text):
        pass

    