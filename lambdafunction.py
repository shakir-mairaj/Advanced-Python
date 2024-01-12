# lambda arguments:expression function that is defined without a name. A lambda function can take any number of
# arguments, but can only have one expression.

addf = lambda x: x + 10
print(addf(5))

mult = lambda x, y: x * y
print(mult(2, 3))

# custom sorting using lambda
points_2 = [(3, 2), (2, -3), (1, 4), (4, 5)]
points_2_sort = sorted(points_2)
points_2_sort_lambda = sorted(points_2, key=lambda x: x[1])  # sort using y index
print(points_2)
print(points_2_sort)
print(points_2_sort_lambda)

list_c = [-3, -5, -2, 1, -4, 2, 7]
sort_c = sorted(list_c)
print(sort_c)
sort_c_lambda = sorted(list_c, key=lambda x: abs(x))
print(sort_c_lambda)

# map function-- map(func, seq), transforms each element with the function.
m = [1, 2, 4, 8]
m_map = map(lambda x: x * x, m)  # square of no using map and lambda
print(list(m_map))

# filter function-- filter(func, seq), returns all elements for which func evaluates to True.
e = [2, 4, 5, 6, 7, 9, 10]
e_filter = filter(lambda x: x % 2 == 0, e)
print(list(e_filter))

f = [1, 2, 4, 6]
f_filter = filter(lambda x: x + 2 == 6, f)
print(list(f_filter))

# reduce- reduce(func, seq), repeatedly applies the func to the elements and returns a single value. func takes 2
# arguments.
from functools import reduce

r = [2, 3, 10]
r_reduce = reduce(lambda x, y: x * y, r)
print(r_reduce)
