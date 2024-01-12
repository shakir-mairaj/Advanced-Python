# Collections: counter,namedtuple,ordereddict,defaultdict,deque
# 1.Counter--stores elements as dictionary keys and their counts as values
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = "aaaabbbbccccddddde"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.items())

list_c = ["a", "2", "c", "d", "c", "a", "a"]
count_l = Counter(list_c)
print(count_l)
# most common items
print(count_l.most_common(1))

print(list(count_l.elements()))

# 2. namedtuple -- assign meaning to each position in tuple,access using name instead of position or index
Point = namedtuple('Point', 'x,y')
pt = Point(1, 4)
print(pt)
print(pt.x, pt.y)

Name = namedtuple('Name', 'a, b')
nm = Name('adam', 'james')
print(nm)

# 3. Ordereddict- OrderedDicts are just like regular dictionaries but they remember the order that items were inserted.
ordinary_dict = {}
ordinary_dict['a'] = 1
ordinary_dict['b'] = 2
ordinary_dict['c'] = 3
ordinary_dict['d'] = 4
ordinary_dict['e'] = 5
# this may be in arbitrary order prior to Python 3.7
print(ordinary_dict)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)
# same functionality as with ordinary dict, but always ordered
for k, v in ordinary_dict.items():
    print(k, v)

# 4. defaultdict--defaultdict will have a default value if that key has not been set yet.
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)
print(d['c'])  # will return default value

# 5. Deque- A deque is a double-ended queue. It can be used to add or remove elements from both ends.
de = deque()
de.append(1)  # append to right
de.append(2)

de.appendleft(3)  # append to left
de.appendleft(4)
print(de)

de.pop()  # remove from right
de.popleft()  # remove from left
print(de)

de.clear()  #remove all elements
print(de)

deq = deque()
deq.extend(['a', 'b', 1])
deq.extendleft(['c', 'd', 2])
print(deq)

deq.rotate(1) #rotate all elements one position to the right
print(deq)
deq.rotate(-2) # rotate all elements 2 position to the left
print(deq)