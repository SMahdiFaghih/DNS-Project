from . import request_handler
from . import security_handler

current_user = None

while (True):
    if (current_user == None):
        print ("Enter Login/Register commands or enter Help command for more info")
        input_parts = input().split()
        if (input_parts[0] == "Register" and len(input_parts) == 5):
            result = request_handler.send_register_request(input_parts[1], input_parts[2], input_parts[3], input_parts[4])
            if (result == True):
                security_handler.generate_new_keys(input_parts[3])
        elif (input_parts[0] == "Login" and len(input_parts) == 3):
            result = request_handler.send_login_request(input_parts[1], input_parts[2])
            if (result == True):
                current_user = input_parts[1]
                security_handler.get_keys(input_parts[1])
        elif (input_parts[0] == "Help"):
            print ("Valid commands are as below:")
            print ("1- Login [username] [password]")
            print ("2- Register [firstname] [lastname] [username] [password]")
        else:
            print ("Wrong command.")
    else:
        print ("Enter mkdir/touch/cd/ls/rm/GetFile/EditFile/LogOut commands or enter Help command for more info")
        input_text = input()
        input_parts = input_text.split()
        if (input_parts[0] == "mkdir" and len(input_parts) == 2):
            request_handler.send_mkdir_request(current_user, input_parts[1].split("/"))
        elif (input_parts[0] == "touch" and len(input_parts) == 2):
            directories = input_parts[1].split("/")[:-1]
            file = input_parts[1].split("/")[-1]
            request_handler.send_touch_request(current_user, directories, file)
        elif (input_parts[0] == "cd" and len(input_parts) == 2):
            request_handler.send_cd_request(current_user, input_parts[1].split("/"))
        elif (input_parts[0] == "ls" and len(input_parts) <= 2):
            if (len(input_parts) == 2):
                request_handler.send_ls_request(current_user, input_parts[1].split("/"))
            else:
                request_handler.send_ls_request(current_user, [])
        elif (input_parts[0] == "rm" and len(input_parts) <= 3):
            if (input_parts[1] == "-r"):
                request_handler.send_rm_directory_request(current_user, input_parts[2].split("/"))
            else:
                request_handler.send_rm_file_request(current_user, input_parts[1].split("/"))
        elif (input_parts[0] == "GetFile" and len(input_parts) == 2):
            directories = input_parts[1].split("/")[:-1]
            file = input_parts[1].split("/")[-1]
            encrypted_data = request_handler.send_get_file_request(current_user, directories, file)
            if (len(encrypted_data) == 0):
                print("")
            else:
                print(security_handler.decrypt(encrypted_data))
        elif (input_parts[0] == "EditFile" and len(input_parts) >= 3):
            input_parts = input_text.split(" ", 2)
            directories = input_parts[1].split("/")[:-1]
            file = input_parts[1].split("/")[-1]
            print(input_parts[2])
            encrypted_data = security_handler.encrypt(input_parts[2])
            request_handler.send_edit_file_request(current_user, directories, file, encrypted_data)
        elif (input_parts[0] == "LogOut" and len(input_parts) == 1):
            request_handler.send_logout_request(current_user)
            current_user = None
        elif (input_parts[0] == "Help"):
            print ("Valid commands are as below:")
            print ("1- mkdir [directory/directory/...]")
            print ("2- touch [directory/directory/.../file]")
            print ("3- cd [directory/directory/...]")
            print ("4- ls [directory/directory/...]")
            print ("5- rm (optional)[-r] [directory/directory/...]")
            print ("6- GetFile [directory/directory/.../file]")
            print ("7- EditFile [directory/directory/.../file] [new data]")
            print ("8- LogOut")
        else:
            print ("Wrong command.")