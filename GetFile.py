import os
import sys

class GetFilePath:
    filter = ['.png', '.bpm', '.jpg']
    paths = []
    names = []

    def __init__(self, root):
        self.dirname = root
        self.__all_path()

    def __all_path(self):
        self.paths = []
        self.names = []

        print('Searching...')
        for maindir, subdir, file_name_list in os.walk(self.dirname):
            for filename in file_name_list:
                filepath = os.path.join(maindir, filename)
                extension = os.path.splitext(filepath)[1]

                if extension in self.filter:
                    self.paths.append(filepath)
                    self.names.append(filename)

    def display_path(self):
        print(self.paths)