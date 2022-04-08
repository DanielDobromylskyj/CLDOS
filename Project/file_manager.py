import storage

# Create

def Create_Folder(path, name):
    StorageAmount = storage.read("Meta")[1]
    done = False
    for file in range(int(StorageAmount)):
        if storage.read(file)[1] == path + name + "/":
            done = False
            break
        elif storage.read(file)[1] == path:
            storage.write(file, path + name + "/")
            Dirs = path.split("/")
            Path = Dirs[0:len(Dirs) - 2]
            Folder_Path = ""
            for folder in Path:
                Folder_Path = Folder_Path + folder + "/"
            Create_Folder(Folder_Path, Dirs[len(Dirs) - 2])
            done = True
            break

    if done:
        return [True, path + name + "/"]
    else:
        return [False, "No Space Left OR Already Foulder There"]

def Create_File(path, name):
    StorageAmount = storage.read("Meta")[1]
    for file in range(int(StorageAmount)):
        # Create A New File Not Change A Folder Into A File
        if storage.read(file)[1] == path:
            storage.write(file, path + name + ".file\n") # Create a new line and that is were the data will be stored (Every line BUT line 1)
            Dirs = path.split("/")
            Path = Dirs[0:len(Dirs)-2]
            Folder_Path = ""
            for folder in Path:
                Folder_Path = Folder_Path + folder + "/"
            Create_Folder(Folder_Path , Dirs[len(Dirs)-2])
            return [True, name + " Created."] # only make 1 file... I need to reset the storage.

    return [False, "File Not Found"]

# Edit / Read

def Open_File(path):
    Amount = storage.read("Meta")[1]
    for file in range(int(Amount)):
        data = storage.read(file)[1]
        AllLines = data.split("\n")
        if AllLines[0].startswith(path):
            Lines = AllLines
            Lines.pop(0)
            output = ""
            for line in Lines:
                output = output + line + "\n"

            output = output[:-1]

            return [True, output]

    return [False, "File Not Found"]


def Open_Folder(path):
    Amount = storage.read("Meta")[1]
    # Get Number Of Folders Before It
    AmountOfFolders = len(path.split("/")) - 1
    Contents = []
    for file in range(int(Amount)):
        data = storage.read(file)[1] # Use The [1] To Only Get Back Data Or Error Message. [0] is for Did It Work (True / False)
        AllLines = data.split("\n")
        if AllLines[0].startswith(path):
            Dirs = AllLines[0].split("/")
            Contents.append(Dirs[AmountOfFolders])

    Contents.pop(len(Contents) - 1) # Remove File Indicator From List (Unneeded)
    return [True, Contents]

# Edit / Write

def Edit_File(path, data):
    Amount = storage.read("Meta")[1]
    WriteData = path + "\n" + data
    for file in range(int(Amount)):
        data = storage.read(file)[1]
        AllLines = data.split("\n")
        if AllLines[0] == path + ".file":
            storage.write(file, WriteData)
            return [True, path + " Edited"]

    return [False, "File Not Found"]

# Delete

def Delete_File(path):
    Amount = storage.read("Meta")[1]
    for file in range(int(Amount)):
        data = storage.read(file)[1]
        AllLines = data.split("\n")
        if AllLines[0] == path:
            storage.write(file, "cldos/") # Reset File. Aka Ready To Use Again
            return [True, path + " Destroyed."]

    return [False, "File Not Found"]

def Delete_Folder(path):
    Amount = storage.read("Meta")[1]
    for file in range(int(Amount)):
        data = storage.read(file)[1]
        AllLines = data.split("\n")
        if AllLines[0].startswith(path):
            Delete_File(AllLines[0])
            return [True, "Deleted All Files In Folder"]

    return [False, "File Not Found"]
