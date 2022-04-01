class OperatingSystem():
    def __init__(self, LongStorage_Amount, RAM_Amount):
        self.scale = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ']

        # Max amount of files - One file = 1 Byte
        self.Secoundary = LongStorage_Amount - 1

        self.RAM = []
        # 2D List Where each 2nd list is a byte: [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(RAM_Amount):
            self.RAM.append([0, 0, 0, 0, 0, 0, 0, 0])

        self.commands = ["LoadApli"]

        # Ready Display
        self.DisplayClear()

    def Wait(self):
        input()

    def UserInput(self, text = "", Return = True, letter_case = None):
        raw_in = input(text)


        if letter_case == None:
            text = raw_in

        elif letter_case == "lower":
            text = raw_in.lower()

        elif letter_case == "upper":
            text = raw_in.upper()


        if Return:
            return text

    # Display Anything

    def DisplayText(self, text):
        print(text)

    def DisplayImage(self, img):
        row_number = 0
        for row in img:
            row_data = ""
            for col in row:
                row_data = row_data + " " + col + " "
            print(row_data)
            row_number += 1

    def DisplayClear(self):
        for i in range(60):
            print("")


    # ---   Storage   ---

    # Dumps
    def Dump_RAM(self):
        return self.RAM

    # Storing

    def Store_RAM(self, location, value):
        if type(value) == list:
            if len(value) == 8:
                self.RAM.pop(location)
                self.RAM.insert(location, value)
            else:
                print("Max Amount Of Bits Per Value Is 8. Min Amount Of Bits Per Value Is 8. You Inputed: ", len(value))
        else:
            print("Value Is Not A List Of Bytes. Your Type: ", type(value))

    def Store_Long(self, location, value, Type = "binlist"):
        # Check If That Location Is Valid
        if int(location) <= self.Secoundary:
            # Check If Its Valid Data
            try:
                location_file = open("Storage/" + str(location) + ".txt", "x")
            except FileExistsError:
                    location_file = open("Storage/" + str(location) + ".txt", "w")

            # Turn List into string / storable data
            if Type == "binlist":
                store = "&!!"
                for Val in value:
                    store = store + str(Val)
            elif Type == "image1":
                store = "!&!1" + str(value)
            else:
                print("Invalid Data Type. Asumming its A List")
                store = "&!!"
                for Val in value:
                    store = store + str(Val)


            location_file.write(store)
            location_file.close()
        else:
            print("Invalid Location - Not Found")

    # Getting

    def Get_RAM(self, location):
        return self.RAM[location]

    def Get_Long(self, location):
        try:
            file = open("Storage/" + str(location) + ".txt", "r")
            value = file.read()
            file.close()

            Type = value[:3]

            # 'binary' Text File Using 1 List
            if Type == "&!!":
                list_value = []
                Data = value[3:]
                for chr in Data:
                    list_value.append(int(chr))

                return list_value

            # Image Format 1
            if Type == "!&!": # Every 25 Chars is a new thing
                if value[:4] == "!&!1":
                    Data = value[4:]
                    return eval(Data)



        except FileNotFoundError:
            return None

    def LoadApli(self, Apli_Name):
        global OS
        print(type(OS))
        exec("from programs import " + str(Apli_Name))
        exec("APLI = " + Apli_Name + ".PROGRAM()")
        exec("APLI.open()")

    def Terminal(self):
        OS.DisplayClear()
        while True:
            command = OS.UserInput(text=">>")
            if command == "LoadApli":
                args = OS.UserInput("Args: ")
                self.LoadApli(args)


class PROGRAM():
    def __init__(self, LongStorage_Amount, RAM_Amount):  # Basic Stuff That Needs Defining.

        self.OS = OperatingSystem(int(LongStorage_Amount), int(RAM_Amount))
        self.scale = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w',
                      'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j',
                      'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>',
                      'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ']

        self.version = "0.1"
        self.publisher = "Daniel Dobromylskyj"
        self.Licence = "MIT"
        self.FullName = "Image Maker Basic - v0.1"

    def Info(self):
        return (self.version, self.FullName, self.publisher, self.Licence)

    def open(self):  # Program Code
        self.alpha = ["A", "B", "C", "D", "E"]
        self.Current_image = [
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]
        ]

        def Update():
            self.OS.DisplayClear()
            print("-- Image Maker v0.1 --")
            print("")
            print("* : -1- -2- -3- -4- -5-")
            row_number = 0
            for row in self.Current_image:
                row_data = self.alpha[row_number] + " : |"
                for col in row:
                    row_data = row_data + " " + col + " |"
                print(row_data)
                row_number += 1

        def Save():
            self.OS.DisplayClear()
            location = self.OS.UserInput(text="Location: ")
            self.OS.Store_Long(location, self.Current_image, Type="image1")

        Update()

        while True:
            print("")
            UserIn = self.OS.UserInput(text="GridLetter GridNumber@@character OR exit / save: ", letter_case='upper')

            if UserIn == 'EXIT':
                break


            elif UserIn == 'SAVE':
                Save()
                self.OS.DisplayClear()
                break

            else:
                try:
                    gridref, char = UserIn.split("@@")
                    if char in self.scale:
                        Letter, col = gridref.split(" ")
                        col = int(col) - 1  # Make it proper for list
                        row = self.alpha.index(Letter)

                        # Change List
                        self.Current_image[row].pop(col)
                        self.Current_image[row].insert(col, str(char))
                        # Update Screen
                        Update()


                except Exception as e:
                    print("Bad Input | Eg: A 2@@#")
                    pass



