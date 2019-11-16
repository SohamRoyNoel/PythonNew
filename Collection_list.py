list1 = [5, 9, 7, 10]
list2 = [1, 4, 3, 2]

list3 = list1+list2
print(list3)
list3.sort()
print(list3)

# illigal ways
list3 = list1+list2
# list3.sort()
print(list3.sort())

list3 = list1+list2
list3.sort()
print(sorted(list3))

list3 = list1+list2
countlist = sorted(list3)
print(countlist)

if list1+list2 == countlist:
    print("they are equal")
else:
    print("they are not equal")

if sorted(list1+list2) == countlist:
    print("they are equal")
else:
    print("they are not equal")
