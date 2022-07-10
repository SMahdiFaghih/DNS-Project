import os

class FileSystemHandler():
    repo_path = "FileRepo/"

    def __init__(self) -> None:
        pass

    def mkdir(self, dir):
        os.mkdir(os.path.join(self.repo_path, dir))