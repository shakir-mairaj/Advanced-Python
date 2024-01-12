# A decorator is a function that takes another function and extends the behavior of this function without explicitly
# modifying it.
# 1. Function decorators
# def start_end_decorator(func):
#     def wrapper():
#         print("Begin")
#         func()
#         print("Finish")
#
#     return wrapper
#
#
# @start_end_decorator
# def print_name():
#     print("Adam")
#
#
# print_name()

# function decorators with arguments
# def decorator_with_arguments(func2):
#     def wrapper(*args, **kwargs):
#         print("Before")
#         result = func2(*args, **kwargs)
#         print("After")
#         return result
#
#     return wrapper
#
#
# @decorator_with_arguments
# def addf(x):
#     return x + 10
#
#
# result = addf(10)
# print(result)

# decorator function arguments-- repeat
import functools


# def repeat(num_times):
#     def decorator_repeat(func3):
#         @functools.wraps(func3)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func3(*args, **kwargs)
#             return result
#
#         return wrapper
#
#     return decorator_repeat
#
#
# @repeat(num_times=3)
# def greet(name):
#     print(f'Hello {name}')
#
#
# greet("James")


# nested decorators
# def start_end_decorator_4(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result
#
#     return wrapper
#
#
# # a decorator function that prints debug information about the wrapped function
# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#
#     return wrapper
#
#
# @debug
# @start_end_decorator_4
# def say_hello(name):
#     greeting = f'Hello {name}'
#     print(greeting)
#     return greeting
#
#
# # now `debug` is executed first and calls `@start_end_decorator_4`, which then calls `say_hello`
# say_hello(name='Alex')

# Class decorators
class countcalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)


@countcalls
def say_hello():
    print('Hello')


say_hello()
