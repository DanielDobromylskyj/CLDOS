import file_manager
import command

class file_access():
    def write_to_file(self, file, data):
        file_manager.Edit_File(file, data)


class terminal():
    def mkdir(self, pathname):
        command.mkdir(pathname)

    def mkfile(self, pathname):
        command.mkfile(pathname)

    def rmdir(self, pathname):
        command.rmdir(pathname)

    def rmfile(self, pathname):
        command.rmfile(pathname)


def compile_windows(pathname, file):
    path, name = command.GetPathInfo(pathname)
    file_manager.Create_File(path, name)
    file_manager.Edit_File(pathname, open(file, "r").read())

if __name__ == "__main__":
    print(" -- Compiler For Windows -- ")
    PathAndName = input("path/to/file/name = ")
    file = input("windows - path/name = ")
    compile_windows(PathAndName, file)
    print("Compiled From Windows.")
