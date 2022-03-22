import pickle

def writeDictToLocalDatabase(databaseName, mydata):
    with open(databaseName+'.db','wb') as openfile:
        pickle.dump(mydata, openfile, protocol=pickle.HIGHEST_PROTOCOL)

def readDictFromLocalDatabase(databaseName):
    with open(databaseName+'.db','rb') as openfile:
        return pickle.load(openfile)

def createDatabase(databaseName):
    with open(databaseName+'.db','wb') as openfile:
        pickle.dump({}, openfile, protocol=pickle.HIGHEST_PROTOCOL)