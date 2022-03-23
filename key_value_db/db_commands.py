import redis

class Commands:
    def __init__(self, host='redis-11787.c212.ap-south-1-1.ec2.cloud.redislabs.com', port=11787 , password='DYCGtrpViyoZmYWCSHhhrmhMIQ1ABTMR'):
        ## This is a testing cloud hosted redis server. The actual db values will be stored as secrests
        self.conn = redis.Redis(host=host, port=port , password=password)
        self.multiCommands = []
        self.isMulti = False
        self.compactCommands = {}

    def checkConnection(self):
        return self.conn.ping()

    def run_all_commands(self):
        try:
            for command in self.multiCommands:
                commandName = command.strip().split()[0]
                getattr(self, commandName)(command)
        except:
            print("Some of the multiline commands failed to execute")


    def MULTI(self, userCommand):
        self.isMulti = True

    def DISCARD(self, userCommand):
        self.isMulti = False
        self.multiCommands = []

    def EXEC(self, userCommand):
        self.isMulti = False
        self.run_all_commands()

    def SET(self, userCommand):
        if self.isMulti:
            self.multiCommands.append(userCommand)
        else:
            try:
                line = userCommand.strip().split()
                self.compactCommands[line[1]] = line[2]
                return self.conn.set(line[1],line[2])
            except:
                return False

    def GET(self, userCommand):
        if self.isMulti:
            self.multiCommands.append(userCommand)
        else:
            try:
                line = userCommand.strip().split()
                output = self.conn.get(line[1])
                print(output)
                return output
            except Exception as e:
                print(e)
                return False

    def DEL(self, userCommand):
        if self.isMulti:
            self.multiCommands.append(userCommand)
        else:
            try:
                line = userCommand.strip().split()
                self.compactCommands.pop(line[1], None)
                return self.conn.delete(line[1])
            except:
                return False

    def INCR(self, userCommand):
        if self.isMulti:
            self.multiCommands.append(userCommand)
        else:
            try:
                line = userCommand.strip().split()
                self.compactCommands[line[1]] = int(self.compactCommands[line[1]]) + 1
                return self.conn.incr(line[1])
            except Exception as e:
                print(e)
                return False

    def INCRBY(self, userCommand):
        if self.isMulti:
            self.multiCommands.append(userCommand)
        else:
            try:
                line = userCommand.strip().split()
                self.compactCommands[line[1]] = int(self.compactCommands[line[1]]) + int(line[2])
                return self.conn.incrby(line[1],line[2])
            except:
                return False
        
    def COMPACT(self, userCommand):
        for key in self.compactCommands.keys():
            print('SET',key,str(self.compactCommands[key]))