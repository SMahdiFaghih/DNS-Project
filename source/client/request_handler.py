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

def send_login_request(username, password):
    request_data = {
        "type": "User",
        "command": "Login",
        "username": username,
        "password": password
        }
    result = handle_request(request_data)
    print (result)