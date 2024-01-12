# itertools: product,permutations,combinations,accumulate,groupby,infinite operators

# 1.Product- This tool computes the cartesian product of input iterables.
from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

# 2. Permutations- permutations of all elements with all possible orderings with no repeated elements
from itertools import permutations

c = [1, 3, 6]
perm = permutations(c)
print(list(perm))

# 3. Combinations- the combination tuples will be produced in sorted order.
# combinations() does not allow repeated elements, but combinations_with_replacement() does.
from itertools import combinations, combinations_with_replacement

d = [5, 6, 7]
comb = combinations(d, 2)  # 2 is the length of output tuples
print(list(comb))

comb_r = combinations_with_replacement(d, 2)
print(list(comb_r))

# 4. accumulate-- accumulate sums or other operations
from itertools import accumulate
import operator

e = [1, 3, 6, 8, 10]
acc = accumulate(e)
print(list(acc))

mul = accumulate(e, func=operator.mul)  # multiplication
print((list(mul)))

# 5. Groupby-- returns consecutive keys and groups from the iterable.
from itertools import groupby


def smaller_than_3(x):
    return x < 3


y = [1, 2, 3, 4, 5]
g = groupby(y, key=smaller_than_3)
for key, value in g:
    print((key, list(value)))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Andy', 'age': 27}, {'name': 'Lisa', 'age': 27},
           {'name': 'Claire', 'age': 28}]

grp_person = groupby(persons, key=lambda x: x['age'])
for key, value in grp_person:
    print(key, list(value))

# 6. Infinite operators- count, cycle, repeat
from itertools import count, cycle, repeat

# count
for i in count(10):
    print(i)
    if i >= 15:
        break
# cycle
cyc = [1, 9, 11]
sum = 0
for i in cycle(cyc):
    print(i)
    sum += i
    if sum >= 25:
        break

# repeat
for i in repeat(cyc, 2):
    print(i)
