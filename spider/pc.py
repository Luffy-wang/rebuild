# product

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
k=0
# for i in fib():
#     print(i)
#     if k<10:
#         k+=1
#     else:
#         break 

#------------------------------------#

#coroutine

def grep(pattern):
    print("start:",pattern)
    while True:
        line=(yield)
        if pattern in line:
            print(line)

# search=grep("hello")
# next(search)
# search.send("my name hi")
# search.send("my name hello")
# search.close()

#---------------------------------------#

#wraps
import logging
from functools import wraps


def mylogwarp(func):
    @wraps(func)
    def dosomething(*args,**kwargs):
        logging.error("hi ,look this")
        return func(*args,**kwargs)
    return dosomething

@mylogwarp
def sayhi():
    print("end")

#sayhi()


#----------------------------------------------#

#wraps 

def logit(logfile='/tmp/session.json'):
    def log_decorator(func):
        @wraps(func)
        def log_log(*args,**kwargs):
            with open(logfile,'a') as f:
                f.write("it call")
                return func(*args,**kwargs)
        return log_log
    return log_decorator

@logit()
def sayhello():
    print("hello")

sayhello()