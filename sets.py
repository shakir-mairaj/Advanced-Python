# Set: unordered,unindexed,mutable and no duplicate elements
# 1. Creating a set
set_1 = {1, 2, 3}
print(set_1)

set_2 = set(("apple", "banana", "cherry"))
print(set_2)

a = {}
b = set(a)
print(type(a))
print(type(b))

# 2. Adding elements in set
set_1.add(20)
set_1.add("orange")
print(set_1)

# 3. Remove elements
set_1.remove("orange")
print(set_1)

set_1.discard(1)
print(set_1)

set_1.clear()  # remove all elements
print(set_1)

# 4. Check if element in set and iterating
if "apple" in set_2:
    print("yes")
else:
    print("no")

for i in set_2:
    print(i)

#5. Union, Intersection
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = evens.intersection(primes)
print(i)

#6. Difference of sets
set_a = {1, 3, 4, 7, 9, 11, 12}
set_b = {2, 3, 5, 7, 10, 13}

diff_a = set_a.difference(set_b)  # elements in set a that are not in set b
print(diff_a)

diff_b = set_b.difference(set_a)
print(diff_b)

diff_c = set_a.symmetric_difference(set_b) # elements that are in a and b but not in both
print(diff_c)

#7. Update Sets
set_a.update(set_b) #adds elements from other set
print(set_a)

set_a.intersection_update(set_b) #Update the set by keeping only the elements found in both
print(set_a)

set_a.difference_update(set_b) # Update the set by removing elements found in another set.
print(set_a)

set_a.symmetric_difference_update(set_b) #Update the set by only keeping the elements found in either set, but not in both
print(set_a)

#8. Copying sets
set_o = {1, 10, 20}
set_cpy = set_o.copy()
print(set_cpy)

#9. Subset, Superset, Disjoint set
set_ss = {1, 2, 3, 4, 5, 6}
set_sd = {1, 2, 3}
print(set_ss.issubset(set_sd))
print(set_sd.issubset(set_ss)) # true if set_sd is subset of ss

print(set_ss.issuperset(set_sd)) #True if set_ss is superset of set sd

set_cd = {7, 9, 11}
print(set_ss.isdisjoint(set_cd)) # true if both sets have no element in common

#10. Frozen set
#frozen set cannot be updated
a = frozenset([1, 3, 5])
print(a)
a.add(7) # not allowed
print(a)
# we can perform union, intersection etc
