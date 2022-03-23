import db_commands

def processInputInCMD(conn):
    print("To Stop enter x")
    print("Enter commands to process below")
    while True:
        userCommand = input(">>")
        if userCommand.lower() == 'x':
            break
        userCommand = userCommand.strip().split()
        result = getattr(db_commands, userCommand[0])(conn, userCommand[1],userCommand[2])
        print(result)