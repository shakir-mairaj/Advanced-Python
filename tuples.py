# Tuple: ordered,immutable and allow duplicate elements
# 1. Creating a tuple
tuple_1 = (1, "Tom", 2)
print(tuple_1)

# paranthesis is optional for tuple
tuple_2 = 3, "Max", True
print(tuple_2)

# Special case: a tuple with only one element needs to have a comma at the end,
# otherwise it is not recognized as tuple
tuple_3 = (5,)
print(tuple_3)

# convert an iterable (list, dict, string) with the built-in tuple function
tuple_4 = tuple([1, 2, 3])
print(tuple_4)

# 2. Access tuple elements
item_t = tuple_1[0]
print(item_t)

item_l = tuple_1[-1]
print(item_l)

# 3. adding or changing tuple item will raise error

# 4. Delete tuple
del tuple_4

# 5. Iterating and checking if an item exists
for i in tuple_2:
    print(i)

if "Max" in tuple_2:
    print("yes")
else:
    print("no")

# 6. Useful methods
print("Length of tuple is", len(tuple_1))
print("Count of character is", tuple_1.count(1))
print("Index of element is", tuple_1.index("Tom"))

tuple_5 = ('a', 'b') * 5  # repetition
print(tuple_5)

# concatenation
concat_tuple = (1, 2, 3) + (4, 5, 6)
print(concat_tuple)

# convert list to a tuple and vice versa and string to tuple
list_t = [1, "Dave", True]
tuple_list = tuple(list_t)
print(tuple_list)

tuple_to_list = list(tuple_list)
print(tuple_to_list)

string_to_tuple = tuple('Hello')
print(string_to_tuple)

# 6. Slicing
c = (1, 2, 3, 4, 5, 6)
d = c[1:3]
print(d)
e = c[:5]
print(e)
f = c[::2]
print(f)
r = c[::-1]
print(r)

# 7. Unpack tuple
# number of variables have to match number of tuple elements
tuple_details = ('Dan', 25, 'NY')
name, age, city = tuple_details
print(name)
print(age)
print(city)

# tip: unpack multiple elements to a list with *
tuple_num = (0, 1, 2, 3, 4, 5, 6)
item_first, *items_between, item_last = tuple_num
print(item_first)
print(items_between)
print(item_last)

# 8. Nested Tuples
tuple_nest = ((1, 2), (3, 4))
print(tuple_nest)

# 9. Compare tuple and list
# size compare
import sys

list_s = [0, 1, 2, 'hello', True]
tuple_s = (0, 1, 2, 'hello', True)
print(sys.getsizeof(list_s), "bytes")
print(sys.getsizeof(tuple_s), "bytes")

# compare the execution time of a list vs. tuple creation statement
import timeit

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
