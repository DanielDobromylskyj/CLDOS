# Lets Try Have This Make A "GUI" Using Symbols

import os

class OperatingSystem():
    def __init__(self, LongStorage_Amount, RAM_Amount):
        self.scale = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ']

        # Max amount of files - One file = 1 Byte
        self.Secoundary = LongStorage_Amount - 1

        self.RAM = []
        self.RAM_Amount = RAM_Amount
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
        for i in range(75):
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
            elif Type == "text":
                store = "!!&" + str(value)

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

            if Type == "!!&":
                return value[3:]



        except FileNotFoundError:
            return None

    def LoadApli(self, Apli_Name):
        try:
            exec("from programs import " + str(Apli_Name))
            exec("APLI = " + Apli_Name + ".PROGRAM(" + str(self.Secoundary) + ", "+ str(self.RAM_Amount) +")")
            exec("APLI.open()")
        except Exception as error:
            if Apli_Name.startswith("-"):
                if Apli_Name == "-list":
                    files = os.listdir('programs')
                    files.remove('__pycache__')
                    print(files)

            else:
                print("Invalide Program Name. Not Found")

    def DisImg(self, location):
        img = OS.Get_Long(location)

        for row in img:
            line = ""
            for col in row:
                line = line + " " + col + " "
            print(line)



class PROGRAM():
    def __init__(self, Long, RAM):
        self.OS = OperatingSystem(Long, RAM)


        self.version = "1"
        self.publisher = "Daniel Dobromylskyj"
        self.Licence = "MIT"
        self.FullName = "Note Editor Basic (No Arrows)"

    def Info(self):
        return (self.version, self.FullName, self.publisher, self.Licence)

    def open(self):
        self.OS.DisplayClear()

        while True:
            AWNS = self.OS.UserInput(text="Load (Say 'None' for blank): ")

            if str(AWNS) == "None":
                TEXT = ""
                print("New Created")
                break
            else:
                TEXT = self.OS.Get_Long(int(AWNS))


                if TEXT == None:
                    print("No File Found")
                else:
                    try:
                        TEXT.split("\n")
                        break
                    except:
                        print("Invalid Format")


        try:

            def Update(TEXT, EditingLine):
                LINES = TEXT.split("\n")
                line_counter = 0
                for line in LINES:
                    if line_counter == EditingLine:
                        line = "> " + str(line) + " <"

                    line_counter += 1
                    print(line)

                changed = input("Line: ")
                if changed == "":
                    pass
                else:
                    try:
                        LINES.pop(EditingLine)
                        LINES.insert(EditingLine, changed)
                    except:
                        LINES.append(changed)

                new_text = ""
                for line in LINES:
                    new_text = new_text + str(line) + "\n"

                new_text = new_text[:-1]

                return new_text





            Line = 0
            while True:
                self.OS.DisplayClear()
                TEXT = Update(TEXT, Line)
                option = self.OS.UserInput("'moveLINENUMBER' OR press 'enter' to continue OR 'save' (or quit)")

                if option.startswith("move"):
                    Line = option[4:]
                elif option == "save":
                    self.OS.DisplayClear()
                    location = self.OS.UserInput(text="Location: ")
                    self.OS.Store_Long(location, TEXT, Type="text")
                    break
                else:
                    pass

        except Exception as e:
            print(e)
