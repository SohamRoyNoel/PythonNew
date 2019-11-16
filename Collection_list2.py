list_1 = list()
list_2 = []
print("List_1 is {}".format(list_1))
print("List_2 is {}".format(list_2))
print(list("the shit is equal"))
if list_1 == list_2:
    print("both ate equal")

print()

even = [2, 4, 6, 8]
another_even = even
another_even.sort(reverse=True)
print(another_even)

print(another_even is even)
# proves sort creats a new list

print()

another_even = list(even)  # pointing different memory
# new list of even, using list constructor
print(another_even is even)

print()

print(another_even == even)  # contains same, but points different list

print()

odd = [1, 3, 5, 7, 9]
new_list = [even, odd]
print((new_list))

for i in new_list:
    print(i)
    for v in i:
        print(v)

print()

new_list_1 = [even+odd]
for x in new_list_1:
    print(x)
    for y in x:
        print(y)
