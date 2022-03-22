from db_read_write import writeDictToLocalDatabase, readDictFromLocalDatabase, createDatabase
from read_input_cmd import inputFromCMD

def _main():
    try:
        data = readDictFromLocalDatabase('mydatabase')
    except FileNotFoundError:
        print("Database not found. Create one before performing operations")
    final_data = inputFromCMD()
    writeDictToLocalDatabase('mydatabase', final_data)

if __name__=="__main__":
    _main()