import terminal
import storage
import command

# Run For First Time Set Up (Doesn't Create program file sor anything just makes space)
Setup = storage.storage()
if Setup:
    command.SetupFiles()

terminal.open()