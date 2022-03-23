import redis

def connDatabase():
    ## This is a testing cloud hosted redis server. The actual db values will be stored as secrests
    r = redis.Redis(host='redis-11787.c212.ap-south-1-1.ec2.cloud.redislabs.com', port=11787 , password='DYCGtrpViyoZmYWCSHhhrmhMIQ1ABTMR')
    return r