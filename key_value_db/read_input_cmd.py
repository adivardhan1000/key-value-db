from db_commands import commands

def parse_string_call_db_commands(comm, userInput):
    '''Reusable to call the db commands
    Inputs: 
        db_commands.commands() Object
        user Input             String'''
    userCommand = userCommand.strip().split()
    return getattr(comm, userCommand[0])(userCommand)


def processInputInCMD(conn):
    print("To Stop enter x")
    print("Enter commands to process below")
    comm = commands(conn)
    while True:
        userCommand = input(">>")
        if userCommand.lower() == 'x':
            break
        print(parse_string_call_db_commands(comm, userCommand))
        