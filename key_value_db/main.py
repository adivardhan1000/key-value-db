from key_value_db.read_input_cmd import processInputInCMD
from key_value_db.db_commands import Commands

def _main():
    # try:
    #     data = readDictFromLocalDatabase('mydatabase')
    # except FileNotFoundError:
    #     print("Database not found. Create one before performing operations")
    # final_data = inputFromCMD()
    # writeDictToLocalDatabase('mydatabase', final_data)
    comm = Commands()
    if comm.checkConnection():
        processInputInCMD(comm)
    else:
        print("Connection Error")

if __name__=="__main__":
    _main()