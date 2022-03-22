from db_commands import *

def inputFromCMD():
    while True:
        userCommand = input("Enter Commands line by line\nTo Stop enter x")
        if userCommand.lower() == 'x':
            break

    return {}