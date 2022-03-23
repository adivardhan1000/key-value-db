from read_input_cmd import processInputInCMD

def _main():
    # try:
    #     data = readDictFromLocalDatabase('mydatabase')
    # except FileNotFoundError:
    #     print("Database not found. Create one before performing operations")
    # final_data = inputFromCMD()
    # writeDictToLocalDatabase('mydatabase', final_data)
    processInputInCMD()

if __name__=="__main__":
    _main()