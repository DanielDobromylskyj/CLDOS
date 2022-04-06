
def RAM(allocated = 1024): # slots
    global SRAM
    SRAM = []
    for i in range(allocated):
        SRAM.append("")


def write(location, value):
    global SRAM
    SRAM[int(location)] = value

def read(location):
    global SRAM
    return SRAM[int(location)]

def read_type(location):
    global SRAM
    return type(SRAM[int(location)])

if __name__ == "__main__":
    RAM()
