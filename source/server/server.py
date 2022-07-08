import os

user_list = []
def find_user(name):
    for user in user_list:
        if user.name == name:
            return user

class User():
    def __init__(self, name) -> None:
        self.name = name
        self.filesystem = FileSystemHandler()
        user_list.append(self)


class FileSystemHandler():
    repo_path = "FileRepo/"

    def __init__(self) -> None:
        pass

    def mkdir(self, dir):
        os.mkdir(os.path.join(self.repo_path, dir))


class ClientHandler:
    def __init__(self) -> None:
        pass

    def handle_request(self, request):
        if request['type'] == 'login':
            username = request['username']
            password = request['password']
            self.authenticate(username, password)
        elif request['type'] == 'change_repo':
            user = find_user['name']
            if request['command_type'] == 'mkdir':
                user.filesystem.mkdir(request['name'])

    def authenticate(self):
        pass
