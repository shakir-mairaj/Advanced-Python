# Generators are functions that return an object that can be iterated over. They generate items one at a time and
# only when asked and are memory efficient
# A generator is defined like a normal function but with the yield statement instead of return.

# def mygenerator():
#     yield 1
#     yield 2
#     yield 3


# g = mygenerator()


# Generator objects execute when next() is called.
# value1 = next(g)  # will print 1
# print(value1)
# value2 = next(g)  # will print 2
# print(value2)
# value3 = next(g)  # will print 3
# print(value3)
#
# for i in g:
#     print(i)

# print(sum(g))

# generator function execution

# def gen1(num):
#     print("Start")
#     while num > 0:
#         yield num
#         num -= 1
#
#
# cd = gen1(5)
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))

# lists vs generator-- memory efficiency
import sys


# lists
def list_n(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


print((sum(list_n(10))))


# generator
def genl(n):
    num = 0
    while num < n:
        yield num
        num += 1


print((sum(genl(10))))

print(sys.getsizeof(list_n(10)))
print(sys.getsizeof(genl(10)))


# Fibonacci sequence using generator
def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib_s = fib(50)
for i in fib_s:
    print(i)

# generator expression-- similar to list comprehension but parenthesis is used
my_gen = (i for i in range(20) if i % 2 == 0)
print(list(my_gen))
