# 1. arguments and parameters
def print_name(name):  # name is parameter
    print(name)


print_name("Tom")  # Tom is argument


# 2. Positional and keyword arguments
def posfunc(a, b, c):
    print(a, b, c)


posfunc(1, 2, 3)  # positional arguments
posfunc(a=1, b=2, c=3)  # keyword arguments
# mix of both
posfunc(1, b=2, c=3)


# not allowed
# posfunc(1,b=2, 3) #positional argument after keyword argument not allowed
# posfunc(1,b=2, a-3) #multiple values for same argument not allowed

# default arguments
def funcd(a, b, c, d=5):
    print(a, b, c, d)


funcd(1, 2, 3)  # d can be left out and it will be still printed. Also default argument should always be defined as the


# last parameter

# Variable length arguments *args and **kwargs
def var_arg(*args, **kwargs):  # *args is for positional arguments and **kwargs is for keyword arguments
    for a in args:
        print(a)
    for k in kwargs:
        print(k, kwargs[k])


var_arg(1, 2, five=5, seven=7)


# Forced keyword arguments
def funf(a, b, *, c, d):  # all parameter after * are keyword arguments
    print(a, b, c, d)


funf(1, 3, c=10, d=11)


# arguments after variable length arguments must be keyword arguments
def funf1(*args, word):
    for v in args:
        print(v)
    print(word)


funf1(2, 7, word=30)


# Unpacking into arguments
def unp(a, b, c):
    print(a, b, c)


# list/tuple unpacking, length must match-- use *
list_1 = [2, 4, 6]
unp(*list_1)

# dict unpacking, keys and length must match-- use **
dict_1 = {'a': '1', 'b': '2', 'c': '3'}
unp(**dict_1)


# global and local variables
def glov():
    x = num
    print("number in function:", x)


num = 0
glov()


def glov1():
    global num  # global variable
    num = 3


print("number before glov1", num)
glov1()
print("number after glov1", num)


