import os

from source.server import security_handler

path = os.path.join(os.path.dirname(__file__), "FileRepo")
if not os.path.exists(path):
    os.mkdir(path)  

class FileSystemHandler():
    def __init__(self) -> None:
        self.repo_path = path

    def mkdir(self, directories):
        temp_path = self.repo_path
        for dir in directories:
            if (dir == "."):
                pass
            elif (dir == ".."):
                temp_path = os.path.join(temp_path, "..")
                if (temp_path != path):
                    temp_path = os.path.abspath(temp_path)
            elif (dir == ""):
                temp_path = path
            else:
                temp_path = os.path.join(temp_path, dir)
                print(temp_path)
                if (not os.path.exists(temp_path) or os.path.isfile(temp_path)):
                    os.mkdir(temp_path)
        return temp_path
    
    def touch(self, directories, file, owner):
        temp_path = self.mkdir(directories)
        file_path = temp_path + "/" + file
        if not os.path.isfile(file_path):
            fp = open(file_path, 'w')
            encrypted_owner = security_handler.encrypt(owner + "\nTesting")
            fp.write(encrypted_owner)
            fp.close()

    def cd(self, directories):
        temp_path = self.repo_path
        for dir in directories:
            temp_path = os.path.join(temp_path, dir)
            if (dir == "."):
                pass
            elif (dir == ".."):
                if (temp_path != path):
                    temp_path = os.path.abspath(temp_path)
            elif (dir == ""):
                temp_path = path
            else:
                if (not os.path.exists(temp_path) or os.path.isfile(temp_path)):
                    return "Directory not exists with name: " + dir 
        self.repo_path = temp_path
        return "Current path is: " + self.repo_path
    
    def ls(self, directories, username):
        temp_path = self.repo_path
        if (len(directories) == 0):
            pass
        else:
            for dir in directories:
                temp_path = os.path.join(temp_path, dir)
                if (dir == "."):
                    pass
                elif (dir == ".."):
                    if (temp_path != path):
                        temp_path = os.path.abspath(temp_path)
                elif (dir == ""):
                    temp_path = path
                else:
                    if not os.path.exists(temp_path):
                        return "Directory not exists with name: " + dir 
        files = []
        for file in os.listdir(temp_path):
            file_path = os.path.join(temp_path, file)
            if (os.path.isfile(file_path)):
                p = open(file_path, 'r')
                file_data = security_handler.decrypt(p.read())
                if (file_data.split("\n")[0] == username):
                    files.append(file)
            else:
                files.append(file)
        data = {
        "current_path": self.repo_path,
        "files": files
        }
        return data
    
    def rm(self, fileOrDirectory, path, username):
        temp_path = self.repo_path
        for dir in path:
            temp_path = os.path.join(temp_path, dir)
            if (dir == "."):
                pass
            elif (dir == ".."):
                if (temp_path != path):
                    temp_path = os.path.abspath(temp_path)
            elif (dir == ""):
                temp_path = path
            else:
                if not os.path.exists(temp_path):
                    return "Directory or File not exists with name: " + dir
        if (os.path.isfile(temp_path) and fileOrDirectory == "File"):
            p = open(temp_path, 'r')
            file_data = security_handler.decrypt(p.read())
            if (file_data.split("\n")[0] == username):
                os.remove(temp_path)
                return "File removed successfully"
            else: 
                return "Directory or File not exists with name: " + dir 
        elif (not os.path.isfile(temp_path) and fileOrDirectory == "Directory"):
            if (len(os.listdir(temp_path)) == 0):
                os.rmdir(temp_path)
                return "Directory removed successfully"             
            else: 
                return "Directory is not empty"
            