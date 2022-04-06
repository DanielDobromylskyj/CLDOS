
def storage(allocated = 1024):
    def Write(allocated):
        for i in range(allocated):
            try:
                open("STORAGE/" + str(i) + ".cldos", "x").write("cldos/")
            except FileExistsError:
                pass
        try:
            f = open("STORAGE/Meta.cldos", "x")
            f.write(str(allocated))
            f.close()
        except:
            f = open("STORAGE/Meta.cldos", "w")
            f.write(str(allocated))
            f.close()

        print("First Time SetUp Complete")


    try:
        f = open("STORAGE/Meta.cldos", "r")
        if int(f.read()) < allocated:
            Write(allocated)

        return False
    except FileNotFoundError:
        Write(allocated)
        return True


def write(location, value):
    try:
        file = open("STORAGE/" + str(location) + ".cldos", "w")
        file.write(value)
        file.close()

        # True - Worked As Intended
        return [True, None]

    except Exception as error:
        return [False, error]

def read(location):
    try:
        file = open("STORAGE/" + str(location) + ".cldos", "r")
        value = file.read()
        file.close()

        # True - Worked As Intended
        return [True, value]

    except Exception as error:
        return [False, error]


if __name__ == "__main__":
    storage(1024)