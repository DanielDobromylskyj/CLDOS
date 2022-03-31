# Lets Try Have This Make A "GUI" Using Symbols

class OperatingSystem():
    def __init__(self, LongStorage_Amount, RAM_Amount):
        self.scale = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ']

        # Max amount of files - One file = 1 Byte
        self.Secoundary = LongStorage_Amount - 1

        self.RAM = []
        # 2D List Where each 2nd list is a byte: [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(RAM_Amount):
            self.RAM.append([0, 0, 0, 0, 0, 0, 0, 0])

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

    def DisplayImage(self, image):
        print("Not Done - ", image)


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

    def Store_Long(self, location, value):
        # Check If That Location Is Valid
        if location <= self.Secoundary:
            # Check If Its Valid Data
            if type(value) == list:
                if len(value) == 8:
                    try:
                        location_file = open("Storage/" + str(location) + ".txt", "x")
                    except FileExistsError:
                        location_file = open("Storage/" + str(location) + ".txt", "w")

                    # Turn List into string / storable data
                    store = ""
                    for Val in value:
                        store = store + str(Val)

                    location_file.write(store)
                    location_file.close()

                else:
                    print("Max Amount Of Bits Per Value Is 8. Min Amount Of Bits Per Value Is 8. You Inputed: ",
                          len(value))
            else:
                print("Value Is Not A List Of Bytes. Your Type: ", type(value))

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
            list_value = []
            for chr in value:
                list_value.append(int(chr))

            return list_value
        except FileNotFoundError:
            return None



OS = OperatingSystem(100, 50)

OS.UserInput(text="press enter to start", Return=False)
OS.Store_RAM(41, [1, 0, 0, 1, 0, 1, 0, 0])
OS.Store_Long(21, [0, 1, 1, 0, 1, 0, 1, 1])

print(OS.Get_RAM(41))
print(OS.Get_Long(21))
print(OS.Get_Long(11))