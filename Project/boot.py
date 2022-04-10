import terminal
import storage
import command
import threading

# Run For First Time Set Up (Doesn't Create program file sor anything just makes space)

def NRS():
    command.PRSU() # PRSU = Ping Reply Set-Up

Setup = storage.storage()
if Setup:
    command.SetupFiles()
    input("Please Restart OS / Computer")
else:
    x = threading.Thread(target=NRS)
    x.start()
    terminal.open()