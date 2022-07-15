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
            path = os.path.join(temp_path, dir)
            if not os.path.exists(path):
                os.mkdir(path)
            temp_path = temp_path + "/" + dir