from . import request_handler
from . import database_handler
from . import security_handler

current_user = None
class User:
    def __init__(self, name, public_key, private_key) -> None:
        self.name = name
        self.public_key = public_key
        self.private_key = private_key
    
    def encrypt(self, input_text):
        pass

    def decrypt(self, input_text):
        pass

while (True):
    if (current_user == None):
        print ("Enter Login/Register commands or enter Help command for more info")
        input_parts = input().split()
        if (input_parts[0] == "Register" and len(input_parts) == 5):
            result = request_handler.send_register_request(input_parts[1], input_parts[2], input_parts[3], input_parts[4])
            if (result == True):
                key = security_handler.generate_new_keys()
                current_user = User(input_parts[3], key[0], key[1])
                database_handler.add_new_key(current_user.name, str(current_user.public_key), str(current_user.private_key))
        elif (input_parts[0] == "Login" and len(input_parts) == 3):
            result = request_handler.send_login_request(input_parts[1], input_parts[2])
            if (result == True):
                key = database_handler.get_keys()
                current_user = User(input_parts[3], key[0], key[1])
        elif (input_parts[0] == "Help"):
            print ("Valid commands are as below:")
            print ("1- Login [username] [password]")
            print ("2- Register [firstname] [lastname] [username] [password]")
        else:
            print ("Wrong command.")
    else:
        print ("Enter mkdir/touch/cd/ls/rm/mv commands or enter Help command for more info")
        input_parts = input().split()
        