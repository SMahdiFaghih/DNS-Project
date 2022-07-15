from . import database_handler
from .filesystem_handler import FileSystemHandler

class User():
    def __init__(self, username) -> None:
        self.username = username
        self.filesystem = FileSystemHandler()

user_list = []
def find_user(username):
    for user in user_list:
        if (user.username == username):
            return user
    return None

def handle_request(request):
    if (request["type"] == "User"):
        if (request["command"] == "Register"):
            firstname = request['firstname']
            lastname = request['lastname']
            username = request['username']
            password = request['password']
            return database_handler.register(firstname, lastname, username, password)      
        elif (request["command"] == "Login"):
            username = request['username']
            password = request['password']
            result = database_handler.login(username, password)
            if (result == False):
                return "Wrong username or password"
            else:
                user = find_user(username)
                if (user is None):
                    user = User(username)
                    user_list.append(user)
                    return "Login done successfully"
                else:
                    return "Already LoggedIn"
        else:
            return "Wrong command"
    elif (request['type'] == "File"):
        user = find_user(request['name'])
        if (request['command'] == 'mkdir'):
            user.filesystem.mkdir(request['directories'])
        elif (request['command'] == 'touch'):
            user.filesystem.touch(request['directories'], request['file'], user.username)
