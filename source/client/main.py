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
                database_handler.add_new_key(input_parts[3], str(key[0]), str(key[1]))
        elif (input_parts[0] == "Login" and len(input_parts) == 3):
            result = request_handler.send_login_request(input_parts[1], input_parts[2])
            if (result == True):
                key = database_handler.get_keys(input_parts[1])
                current_user = User(input_parts[1], key[0], key[1])
        elif (input_parts[0] == "Help"):
            print ("Valid commands are as below:")
            print ("1- Login [username] [password]")
            print ("2- Register [firstname] [lastname] [username] [password]")
        else:
            print ("Wrong command.")
    else:
        print ("Enter mkdir/touch/cd/ls/rm/mv commands or enter Help command for more info")
        input_parts = input().split()
        if (input_parts[0] == "mkdir" and len(input_parts) == 2):
            request_handler.send_mkdir_request(current_user.name, input_parts[1].split("/"))
        elif (input_parts[0] == "touch" and len(input_parts) == 2):
            directories = input_parts[1].split("/")[:-1]
            file = input_parts[1].split("/")[-1]
            request_handler.send_touch_request(current_user.name, directories, file)
        elif (input_parts[0] == "Help"):
            print ("Valid commands are as below:")
            print ("1- mkdir [directory/directory/...]")
            print ("2- Register [firstname] [lastname] [username] [password]")
        else:
            print ("Wrong command.")