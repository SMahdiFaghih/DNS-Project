from . import request_handler

current_user = None

def handle_input(input):
    print (input)

while (True):
    if (current_user == None):
        print ("Enter Login or Register commands or enter Help command for more info")
        input_parts = input().split()
        if (input_parts[0] == "Login" and len(input_parts) == 3):
            request_handler.send_login_request(input_parts[1], input_parts[2])
        elif (input_parts[0] == "Register" and len(input_parts) == 5):
            request_handler.send_register_request(input_parts[1], input_parts[2], input_parts[3], input_parts[4])
        elif (input_parts[0] == "Help"):
            print ("Valid commands are as below:")
            print ("1- Login username password")
            print ("2- Register firstname lastname username password")
        else:
            print ("Wrong command.")
    else:
        print ("Enter mkdir or commands")
        input_text = input()
        handle_input(input_text)

class User:
    def __init__(self, name, public_key, private_key) -> None:
        self.name = name
        self.public_key = public_key
        self.private_key = private_key
    
    def encrypt(self, input_text):
        pass

    def decrypt(self, input_text):
        pass
