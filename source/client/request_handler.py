from .names_security_handler import *
from ..server.client_handler import handle_request

def send_register_request(firstname, lastname, username, password):
    request_data = {
        "type": "User",
        "command": "Register",
        "firstname": firstname,
        "lastname": lastname,
        "username": username,
        "password": password
        }
    result = handle_request(request_data)
    print (result)
    return result == "Registeration done successfully"

def send_login_request(username, password):
    request_data = {
        "type": "User",
        "command": "Login",
        "username": username,
        "password": password
        }
    result = handle_request(request_data)
    print (result)
    return result == "Login done successfully"

def send_logout_request(username):
    request_data = {
        "type": "User",
        "command": "LogOut",
        "username": username
        }
    result = handle_request(request_data)
    print (result)
    return result == "Login done successfully"

def send_mkdir_request(username, directories):
    directories = encryptAll(directories)
    request_data = {
        "type": "File",
        "command": "mkdir",
        "name": username,
        "directories": directories
        }
    handle_request(request_data)
    print ("Folders created successfully")

def send_touch_request(username, directories, file):
    directories = encryptAll(directories)
    file = encrypt(file)
    request_data = {
        "type": "File",
        "command": "touch",
        "name": username,
        "directories": directories,
        "file": file
        }
    result = handle_request(request_data)
    print (result)

def send_cd_request(username, directories):
    directories = encryptAll(directories)
    request_data = {
        "type": "File",
        "command": "cd",
        "name": username,
        "directories": directories
        }
    result = handle_request(request_data)
    if (result[1] == "Error"):
        print (result[0])
    else:
        path = "/".join(decryptAll(result[0].split("\\")))
        print ("Current path is: FileRepo" + path)

def send_ls_request(username, directories):
    directories = encryptAll(directories)
    request_data = {
        "type": "File",
        "command": "ls",
        "name": username,
        "directories": directories
        }
    result = handle_request(request_data)
    if (type(result) is str):
        print (result)
    else:
        path = "/".join(decryptAll(result["current_path"].split("\\")))
        print ("Current path is: FileRepo" + path)
        print ("Files and Directories:")
        result["files"] = decryptAll(result["files"])
        for file in result["files"]:
            print(file)
    
def send_rm_directory_request(username, path):
    path = encryptAll(path)
    request_data = {
        "type": "File",
        "command": "rm",
        "name": username,
        "fileOrDirectory": "Directory",
        "path": path
        }
    result = handle_request(request_data)
    print (result)

def send_rm_file_request(username, path):
    path = encryptAll(path)
    request_data = {
        "type": "File",
        "command": "rm",
        "name": username,
        "fileOrDirectory": "File",
        "path": path
        }
    result = handle_request(request_data)
    print (result)

def send_get_file_request(username, directories, file):
    directories = encryptAll(directories)
    file = encrypt(file)
    request_data = {
        "type": "File",
        "command": "GetFile",
        "name": username,
        "directories": directories,
        "file": file
        }
    result = handle_request(request_data)
    if (result[1] == "Error"):
        print (result[0])
        return ""
    else:
        return result[0]

def send_edit_file_request(username, directories, file, data):
    directories = encryptAll(directories)
    file = encrypt(file)
    request_data = {
        "type": "File",
        "command": "EditFile",
        "name": username,
        "directories": directories,
        "file": file,
        "data": data
        }
    result = handle_request(request_data)
    print (result)   