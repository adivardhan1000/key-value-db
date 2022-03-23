def SET(conn, key, value=0):
    try:
        return conn.set(key,value)
    except:
        return False

def GET(conn, key, value=0):
    try:
        return conn.get(key)
    except:
        return False

def DEL(conn, key, value=0):
    try:
        return conn.delete(key)
    except:
        return False

def INCR(conn, key, value = 1):
    try:
        return conn.incr(key,value)
    except:
        return False

def INCRBY(conn, key, value = 1):
    try:
        return conn.incr(key,value)
    except:
        return False