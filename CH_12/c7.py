import time

def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorator
def f1(func_name):
    print("This is a function" + func_name)

@decorator
def f2(func_name1, func_name2):
    print("This is a function" + func_name1 + func_name2)

@decorator
def f3(func_name1, func_name2, **kw):
    print("This is a function" + func_name1 + func_name2)
    print(kw)


f3('dsa', 'dsda', a=1, b=2, c='dsa')


# f1('func_name')
# f2('das', 'dasd')