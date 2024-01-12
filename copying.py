# Shallow copy and deep copy
# shallow copies: Only one level deep.
#  deep copies: A full independent clone for nested object

# 1. Shallow copy-- done using copy.copy()
import copy

list_a = [10, 20, 30]
list_c = copy.copy(list_a)
print(list_a)
list_c[1] = 50  # it won't affect original list
print(list_c)

list_n = [[2, 3, 6], [9, 8, 7]]
list_nc = copy.copy(list_n) # in this case it will affect the original list too due to nested
list_nc[0][1] = 11
print(list_n)
print(list_nc)

#2. Deep copy
list_dc = copy.deepcopy(list_n) # deep copy will work in case of nested objects, won't affect original list
list_dc[0][2] = 14
print(list_n)
print(list_dc)
