import random
import datetime as dt

def otpgenerate():
    rn=random.randint(100000,1000000)
    timeinfo=dt.datetime.now()
    return rn,timeinfo