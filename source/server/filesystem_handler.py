import os

path = os.path.join(os.path.dirname(__file__), "FileRepo")
if not os.path.exists(path):
    os.mkdir(path)

class FileSystemHandler():
    def __init__(self) -> None:
        self.repo_path = path

    def mkdir(self, directories):
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
                    os.mkdir(path)
        return temp_path
    
    def touch(self, directories, file, owner):
        temp_path = self.mkdir(directories)
        file_path = temp_path + "/" + file
        if not os.path.isfile(file_path):
            fp = open(file_path, 'w')
            fp.write(owner)
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
    
    def ls(self, directories):
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
        data = {
        "current_path": self.repo_path,
        "files": os.listdir(temp_path)
        }
        return data
            