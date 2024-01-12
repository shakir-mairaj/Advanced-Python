# errors and exceptions
# syntax error
# a = 5 print(a)

# type error
# b = 10 + 'c'
# print(b)

# modulenotfounderror
# import somemodule

# Name error
# x = 10
# y = x + z

# filenotfounderror
# f = open("abc.txt")

# value error and index error
# l = [1, 2, 3]
# m = l[4] #index error
# n = l.remove(4) #value error
# print(m)
# print(n)

# key error
# dict = {"name": "tom"}
# print(dict['age'])

# Raising an exception and assert
# x = -10
# if x <= 0:
#     raise Exception("x is not positive")

# y = 3
# assert (y % 2 == 0), 'y is not even number'

# Handling Exceptions
# try:
#     a = 5 / 1
#     b = 4 + 5
#
# except ZeroDivisionError as e:
#     print("zero division error occured", e)
#
# except TypeError as t:
#     print("Type error occured", t)
#
# else:
#     print("No exception error occured")
#
# finally:  # will always run whether there is an exception or not
#     print("Finished")


# Creating own exception
class valuetoohigherror(Exception):
    pass


class valuetoosmallerror(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 1000:
        raise valuetoohigherror('Value is too large')
    if x < 50:
        raise valuetoosmallerror('Value is too small', x)


try:
    test_value(20)
except valuetoohigherror as e:
    print(e)
except valuetoosmallerror as e:
    print(e.message, e.value)
