from db_commands import Commands

def parse_string_call_db_commands(comm, userCommand):
    '''Reusable to call the db commands
    Inputs: 
        db_commands.commands() Object
        user Input             String'''
    commandName = userCommand.strip().split()[0]
    return getattr(comm, commandName)(userCommand)


def processInputInCMD(comm):
    print("To Stop enter x")
    print("Enter commands to process below")
    while True:
        userCommand = input(">>")
        if userCommand.lower() == 'x':
            break
        try:
            output = parse_string_call_db_commands(comm, userCommand)
        except Exception as e:
            print("Error", e)
        