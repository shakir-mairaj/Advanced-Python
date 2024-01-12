# set of functions that are used to generate or manipulate random numbers.
import random

# random float in [0,1)
a = random.random()
print(a)

# random float in range [a,b]
b = random.uniform(1, 10)
print(b)

# random integer in range [a,b]. b is included
c = random.randint(2, 5)  # 5 is included
print(c)

# random integer in range [a,b). b is excluded
d = random.randrange(2, 10)  # 10 is not included
print(d)

# random float from a normal distribution with mu and sigma
e = random.normalvariate(0, 1)
print(e)

# choose a random element from a sequence
f = ["A", "B", "C", "D", "E", "F"]
g = random.choice(f)
print(g)

# choose k unique random elements from a sequence
h = random.sample(f, 3)
print(h)

# choose k elements with replacement, and return k sized list
i = random.choices(f, k=3)
print(i)

# shuffle
random.shuffle(f)
print(f)

# seed generator- With random.seed(), you can make results reproducible
random.seed(1)
print(random.random())
print(random.randint(1, 10))
print(random.uniform(1, 5))

random.seed(1)
print(random.random())
print(random.randint(1, 10))
print(random.uniform(1, 5))

# secrets- used for generating strong numbers typically for passwords,security
import secrets

# random integer in range [0, n).
sec = secrets.randbelow(15)
print(sec)

# return an integer with k random bits.
secb = secrets.randbits(20)
print(secb)

# choose a random element from a sequence
secr = secrets.choice(f)
print(secr)

# numpy random numbers- Create random numbers for nd arrays.
import numpy as np

# np.random.seed(1)
n = np.random.rand(3)
print(n)

v = np.random.randint(10, 20, 4)  # range 10 to 20 with size 4
print(v)

w = np.random.randn(3)
print(w)

arr = np.array([[1, 4, 6], [2, 7, 9], [3, 5, 6]])
np.random.shuffle(arr)
print(arr)
