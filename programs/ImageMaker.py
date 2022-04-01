class ImageMaker():
    def __init__(self, OS):  # Basic Stuff That Needs Defining.
        self.OS = OS
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



