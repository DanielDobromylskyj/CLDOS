import command as cm


def help():
    print("command, args - desc")
    print("seek, path - Shows Dir Contents")
    print("mkdir, path with name - Makes Dir")
    print("mkfile, path with name - Makes File")
    print("rmdir, path - Remove A Dir And Contents")
    print("rmfile, path - Remove A File")
    print("imp, file path - Runs A External File")

def open():
    commands = ["seek", "mkdir", "mkfile", "rmdir", "rmfile", "rdfile", "imp"]
    print("> CLDOS - Comand Line Driven Operating System <")
    print("")
    print("Copyright @ Daniel Dobromylskyj")
    print("")
    while True:
        UserIn = input(">>")


        if UserIn == "exit":
            break
        elif UserIn == "help":
            help()
        elif UserIn == "":
            pass
        else:
            if UserIn in commands:
                Args = input("Args: ")
                try:
                    exec("cm." + str(UserIn) + "('" + Args + "')")
                except Exception as e:
                    print(e)
            else:
                print("Unknown Command Try 'help'")

if __name__ == "__main__":
    open()