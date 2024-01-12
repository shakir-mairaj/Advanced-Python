# 1. Creating a list
list_1 = ['apple', 1, True]
print(list_1)

# 2. Access list elements-- indices start at 0
item = list_1[0]  # 1st element
print(item)

item2 = list_1[-1]  # last element
print(item2)

# 3. Change items
list_1[1] = 25
print(list_1)

# 4. Useful methods
# len()- get number of elements in a list
print("Length of list is ", len(list_1))

# append()-- append item at the end of list
list_1.append('orange')

# insert()-- insert element at a specified position
list_1.insert(0, 'grapes')
print(list_1)

# pop()--removes item in the list at any position,default is the last one
list_1.pop()
print(list_1)

# remove()--remove an item in the list
list_2 = ['pea', 4, False]
list_2.remove(4)
print(list_2)

# clear()--remove all items in the list
list_2.clear()
print(list_2)

# reverse()--reverse items in the list
list_1.reverse()
print(list_1)

# sort()-- to sort a list
list_3 = [3, 2, 10, 1, 4]
list_3.sort()
print("Sorted list is", list_3)

# sorted()-- to get a new sorted list without affecting original
list_4 = ['kiwi', 'melon', 'apple', 'pineapple']
list_sorted = sorted(list_4)
print(list_sorted)

# create list with repeated elements
list_zeroes = [0] * 5
print(list_zeroes)

# concatenation
list_concat = list_4 + list_zeroes
print(list_concat)

# convert string to list
string_list = list('Hello')
print(string_list)

# 5. Copy a List
list_org = ['mint', 'coriander', 'chilli']
list_cpy = list_org

list_cpy.append('carrot')
# modifying copy affects original also in this case
print(list_org)
print(list_cpy)

# use copy() to actually copy the list without modifying original
list_org1 = [1, 2, 3]
list_copy = list_org1.copy()
list_copy.append(5)
print(list_org1)
print(list_copy)

# 6. Iterating
for i in list_1:
    print(i)

# 7. Check if an item exists
if "apple" in list_1:
    print('yes')
else:
    print("No")

# 8. Slicing-- access sub parts of list a[start:stop:step]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[1:3]  # from 2 to 3
print(b)
c = a[2:]  # start from 2nd to end
print(c)
d = a[:5]  # from start to 5th
print(d)
e = a[::2]  # after every 2nd step
print(e)
r = a[::-1]  # reverse list
print(r)
p = a[:]  # copy using slicing
print(p)

# 9. List Comprehension
s = [1, 2, 3, 4, 5]
t = [i * i for i in s]
print(t)

# 10. Nested lists
l = [[1, 2], [3, 4]]
print(l[0])
