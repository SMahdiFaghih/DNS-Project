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

def send_mkdir_request(username, directories):
    request_data = {
        "type": "File",
        "command": "mkdir",
        "name": username,
        "directories": directories
        }
    result = handle_request(request_data)
    print (result)

def send_touch_request(username, directories, file):
    request_data = {
        "type": "File",
        "command": "touch",
        "name": username,
        "directories": directories,
        "file": file
        }
    result = handle_request(request_data)
    print (result)