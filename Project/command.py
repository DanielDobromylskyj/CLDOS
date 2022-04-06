import file_manager

# Viewing / Moving

def seek(path):
    for Object in file_manager.Open_Folder(path)[1]:
        print(Object)

def move(location):
    pass

# Executing Code / External Programs

def imp(file):
    worked, code = file_manager.Open_File(file)
    if worked == True:
        exec(code)
    else:
        print("Error When Getting Data From File")
        print("Got This Error: ", code)

# File Management And Other Non-Terminal Commands

def GetPathInfo(path):
    Dirs = path.split("/")
    name = Dirs[len(Dirs) - 1]
    Dirs.pop(len(Dirs) - 1)
    path = ""
    for part in Dirs:
        path = path + part + "/"
    return path, name

def SetupFiles():
    mkdir("cldos/program files")
    mkdir("cldos/home")

    mkfile("cldos/program files/test")
    mkfile("cldos/home/Welcome")

    file_manager.Edit_File("cldos/program files/test.file", 'print("External File Is Working")\nprint("Multipule Lines Are Work")')
    file_manager.Edit_File("cldos/home/Welcome.file", "Hi! I hope you will enjoy messing around with this OS if you can really call it that! :)")

    print("Complete! Booting Into Terminal.")

def mkdir(pathname):
    path, name = GetPathInfo(pathname)
    print(path, " | ", name)
    print(file_manager.Create_Folder(path, name)[1])

def mkfile(pathname):
    path, name = GetPathInfo(pathname)
    print(file_manager.Create_File(path, name)[1])

def rmdir(path):
    print(file_manager.Delete_Folder(path)[1])

def rmfile(path):
    print(file_manager.Delete_File(path)[1])

def rdfile(path):
    print(file_manager.Open_File(path)[1])


if __name__ == "__main__":
    seek("cldos/program files/")