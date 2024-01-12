# Dictionary: key value pairs, unordered and mutable
# 1. Creating a dictionary
my_dict = {"name": "Tom", "age": 20, "city": "New york"}
print(my_dict)

# using the dict constructor, note: no quotes necessary for keys
dict_2 = dict(name="Lee", age=27, city="LA")
print(dict_2)

# 2. Access items
name_in_dict = my_dict["name"]
print(name_in_dict)

# 3. Adding or updating values
my_dict["email"] = "abc@gmail.com"
print(my_dict)

# 4. Delete items
del my_dict["city"]
print(my_dict)

# this returns the value and removes the key-value pair
print("popped value:", my_dict.pop("age"))

# return and removes the last inserted key-value pair
# (in versions before Python 3.7 it removes an arbitrary pair)
print("popped item:", my_dict.popitem())

print(my_dict)

# clear() : remove all pairs
# my_dict.clear()

# 5. check for keys
dict_3 = {"name": "david", "age": 30, "city": "Ohio"}
if "name" in dict_3:
    print(dict_3["name"])

try:
    print(dict_3["firstname"])
except KeyError:
    print("key not found")

#6. Looping through dictionary
for key in dict_3:
    print(key, dict_3[key])

for key in dict_3.keys():
    print(key)

for value in dict_3.values():
    print(value)

for key, value in dict_3.items():
    print(key, value)

#7. Copying a dictionary
dict_org = {"name": "andy", "age": 34, "city": "DYC"}
dict_cpy = dict_org
dict_cpy["name"] = "kane"
# now modifying the copy also affects the original
print(dict_org)
print(dict_cpy)

# use copy(), or dict(x) to actually copy the dict
dict_copy1 = dict_org.copy()
#dict_copy1 = dict(dict_org)
dict_copy1["name"] = "Monica"
print(dict_org)
print(dict_copy1)

#8. Merging dictionaries
# Use the update() method to merge 2 dicts
# existing keys are overwritten, new keys are added
dict_org.update(dict_copy1)
print(dict_org)

# 9. Possible key types
# use numbers as key, but be careful
my_dict = {3: 9, 6: 36, 9:81}
# do not mistake the keys as indices of a list, e.g my_dict[0] is not possible here
print(my_dict[3], my_dict[6], my_dict[9])

# use a tuple with immutable elements (e.g. number, string)
my_tuple = (8, 7)
my_dict = {my_tuple: 15}

print(my_dict[my_tuple])
# print(my_dict[8, 7])

# a list is not possible because it is not immutable
# this will raise an Error:
# my_list = [8, 7]
# my_dict = {my_list: 15}

#10. Nested Dictionaries
my_dict_1 = {"name": "mary", "age": 29, "city": "LYD"}
my_dict_2 = {"name": "andrew", "age": 31, "city": "MYD"}

nested_dict = {"dict_a": my_dict_1, "dict_b": my_dict_2}
print(nested_dict)
