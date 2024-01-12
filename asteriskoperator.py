# Asterisk operator uses
# Multiplication and power operations
mult = 5 * 10
print(mult)

power = 3 ** 4
print(power)

# creation of list/tuple/string with repeated elements
# list
c_list = [0] * 5
print(c_list)

c_tuple = (1, 3) * 10
print(c_tuple)

c_string = "AB" * 4
print(c_string)


# *args and ** kwargs (variable length and keyword arguments)
def argkwarg(*args, **kwargs):
    for a in args:
        print(a)
    for k in kwargs:
        print(k, kwargs[k])


argkwarg(1, 3, five=5)


# unpacking function arguments
def unpack(a, b, c):
    print(a, b, c)


u_list = [2, 5, 10]
unpack(*u_list)

u_dict = {"a": "10", "b": "20", "c": "30"}
unpack(**u_dict)

#unpacking arguments
num = (1, 3, 5, 7, 9, 11)
*beginning, last = num
print(beginning)
print(last)

beginning, *last = num
print(beginning)
print(last)

beginning, *middle,last = num
print(beginning)
print(middle)
print(last)

#merging iterables,list dictionaries
l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
m_l = [*l_1, *l_2]
print(m_l)

d_1 = {"a": "1", "b": "2"}
d_2 = {"c": "3", "d": "4"}
m_d = {**d_1, **d_2}
print(m_d)


