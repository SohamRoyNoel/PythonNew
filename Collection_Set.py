
# alike DICTIONARY pass all elements WITHOUT A KEY...................
py_set = {"shit", "bra", "panti", "bikini"}
print(py_set)

print()
# using SET function, and passing elements like LIST ["E1","E2","E3", ...... "En"]
py_set2 = set(["shit", "bra", "panti", "bikini"])
print(py_set2)

for i in py_set2:
    print(i)


py_set2.add("DILDO")
py_set.add("DILDO")
# this will never gives op IN SAME ORDER
print(py_set)
print(py_set2)


# An empty set can not be formed useing (), instade it creates a DICTIONARY
empty_set = set()
print(empty_set)


# though an empty set {} creates a DICTIONARY instade of set,
# so .add method wont work here
empty_set.add("a")
print(empty_set)

empty_set2 = {}
# empty_set2.add("a")
# print(empty_set2) #error


# TUPLE to SET
tup = (1, 2, 5, 8, 9,)
set_tup = set(tup)
print(set_tup)


# union and intersection operation
even_no = set(range(0, 30, 2))
print(even_no)
print(len(even_no))
print()
tup2 = (1, 5, 8, 10, 16, 9)
nos = set(tup2)
print(nos)
print(len(nos))

print("inter")
# intersection
inter = even_no.intersection(tup2)
print(inter)
print(len(inter))

print("union")
union = even_no.union(tup2)
print(union)
print(len(union))


print(even_no & nos)  # intersection


# sorting a set coz it never gurenties the same value in same order
# using the set values as before [even_no] & [nos]
# print(even_no.sort()) -- wrong
print(sorted(even_no))
print(sorted(nos))
# becomes stable in case of order


# subtracting sets
# even_no - nos
print(sorted(even_no.difference(nos)))
print(sorted(even_no-nos))


# nos-even_no
print(sorted(nos.difference(even_no)))
print(sorted(nos-even_no))


# difference_update : deletes all the same things from even_no with
# respect to nos
print(sorted(even_no))
print(sorted(nos))
# returns None bcz it doesnt have a return type
print(even_no.difference_update(nos))
print(nos.difference_update(even_no))
even_no.difference_update(nos)
print(even_no)
nos.difference_update((even_no))
print(nos)


# symmetric_difference() -> deletes element from list that are identical
# #AND NON IDENTIALS ARE INSERTED in one shot
print(sorted(even_no))
print(sorted(nos))
print(sorted(even_no.symmetric_difference(nos)))
print(sorted(nos.symmetric_difference(even_no)))


#remove and discard
# remove throws an error if the element doesnt exist
# discard doesnt give any error if the element doesnt exist
print(nos)
nos.remove(1)
nos.discard(5)
print(nos)
print()
nos.discard(20)  # no error
# nos.remove(20) #error
print(nos)


if a.issubset(b):
    print("a is a subset of b")
else:
    print("b is a subset of a")

if b.issuperset(a):
    print("b is a superset of a")
else:
    print("a is a superset of b")


# Frozen Set : immutable set : a set that cnt be changed
# frozen key can be usedas a dictionary key
# frozen set can also be added as a member of a set
# no ADD REMOVE DISCARD is available in frozen set
# UNION INTERSECTION SUBTRACTION ALL ARE ALLOWED IN FROZEN SET, LIKE OTHER
P = frozenset(range(0, 20, 2))
print(P)
