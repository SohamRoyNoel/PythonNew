
my_range = range(0, 100)
print(my_range)  # generates a range object


nos = list(range(0, 10))
print(nos)


even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)


ms_str = "abcdefghijklmnopqrstuvwxyz"
print(ms_str.index("c")+1)  # bc it starts from 0
print(ms_str[2])


small = range(0, 10)
print(small.index(6))
print(small[6])


# if divisible by 7

seven = range(7, 100, 7)  # 7 to 1000, increment by 7
x = int(input("enter any val : "))
if x in seven:
    print("{} is divisible by 7".format(x))


my = small[::2]  # applying on an existing range that has no incremt val
print(my)
print(my.index(8))  # 0,2,4,6,8


dec = range(0, 100)
print(dec)
new_dec = dec[3:30:5]
print(new_dec)


for i in new_dec:
    print(i)


for i in range(3, 30, 5):
    print(i)


print(new_dec == range(3, 30, 5))
