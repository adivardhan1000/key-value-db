import redis

class Commands:
    def __init__(self):
        ## This is a testing cloud hosted redis server. The actual db values will be stored as secrests
        self.conn = redis.Redis(host='redis-11787.c212.ap-south-1-1.ec2.cloud.redislabs.com', port=11787 , password='DYCGtrpViyoZmYWCSHhhrmhMIQ1ABTMR')
        self.commands = []
        self.isMulti = False

    def run_all_commands(self):
        try:
            for command in self.commands:
                commandName = command.strip().split()[0]
                getattr(self, commandName)(command)
        except:
            print("Some of the multiline commands failed to execute")


    def MULTI(self, userCommand):
        self.isMulti = True

    def DISCARD(self, userCommand):
        self.isMulti = False
        self.commands = []

    def EXEC(self, userCommand):
        self.isMulti = False
        self.run_all_commands()

    def SET(self, userCommand):
        if self.isMulti:
            self.commands.append(userCommand)
        else:
            try:
                line = userCommand.strip().split()
                return self.conn.set(line[1],line[2])
            except:
                return False

    def GET(self, userCommand):
        if self.isMulti:
            self.commands.append(userCommand)
        else:
            try:
                line = userCommand.strip().split()
                return self.conn.get(line[1])
            except Exception as e:
                print(e)
                return False

    def DEL(self, userCommand):
        if self.isMulti:
            self.commands.append(userCommand)
        else:
            try:
                line = userCommand.strip().split()
                return self.conn.delete(line[1])
            except:
                return False

    def INCR(self, userCommand):
        if self.isMulti:
            self.commands.append(userCommand)
        else:
            try:
                line = userCommand.strip().split()
                return self.conn.incr(line[1])
            except:
                return False

    def INCRBY(self, userCommand):
        if self.isMulti:
            self.commands.append(userCommand)
        else:
            try:
                line = userCommand.strip().split()
                return self.conn.incrby(line[1],line[2])
            except:
                return False
        