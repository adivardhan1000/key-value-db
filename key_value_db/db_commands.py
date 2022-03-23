class commands:
    def __init__(self,conn):
        self.conn = conn
        self.commands = []
        self.isMulti = False

    def parse_command(comm, userCommand):
        userCommand = userCommand.strip().split()
        if len(userCommand) == 1:
            result = getattr(comm, userCommand[0])(userCommand[1],userCommand[2])

    def MULTI(self,userCommand):
        self.isMulti = True

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
            except:
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
                return self.conn.incr(line[1],line[2])
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
        