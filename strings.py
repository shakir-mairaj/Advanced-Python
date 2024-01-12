# Strings: ordered,immutable, text representation
# 1. String creation
str_1 = "Hello"  # single or double quotes
print(str_1)

str_2 = 'I\' m a human'
print(str_2)

# multiline
str_3 = """Hello  
World"""
print(str_3)

str_4 = "Hello\
        World"
print(str_4)

# 2. Access characters and strings
c = str_1[0]
print(c)

d = str_1[1:3]
print(d)

e = str_1[:5]
print(e)

r = str_1[::-1]
print(r)

# 3. Concatenate
str_co = "Good"
str_do = "Morning"
str_codo = str_co + ' ' + str_do
print(str_codo)

# 4. Iteration and check in a string
for i in str_1:
    print(i)

if "H" in str_1:
    print("yes")
else:
    print("no")

# 5. Useful methods
str_w = "    evening   "
print(str_w.strip())  # remove whitespace

# length
print("Length of string is", len(str_w))

# upper and lower case
print("upper case is ", str_w.upper())
print("lower case is", str_w.lower())

# starts and ends with
str_se = "Adventure"
print(str_se.startswith("Ad"))
print(str_se.endswith("re"))

# index of character
print("Index of v is", str_se.find('v'))

# count number of characters
print("count of char is ", str_se.count('e'))

# replace string
str_df = "How are you feeling"
str_df1 = str_df.replace("feeling", "doing")
print(str_df1)

# split string into list
print("Split string is", str_df.split())

# join list into a string
list_str = ["I", "am", "doing", "fine"]
j = ' '.join(list_str)  # joined using space
print(j)

#Formatting
var = "Tom"
my_str = "The variable is %s" % var
print(my_str)

#f-strings
val1 = 2
val2 = 3.14222
f_string = f"the variables are {val1} and {val2}"
print(f_string)
g = f"The value is {2*50}"
print(g)