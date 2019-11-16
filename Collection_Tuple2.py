
tup1 = "A", "B", "C"
tup2 = "d", "e", "f"
tup3 = "g", "h", "i"

print(tup3)

tup4 = "g", "h", "i", (("j", "k"), ("L", "M"), ("N", "O"), ("P", "Q"))
print(tup4)

tup5 = "g", "h", "i", (("j", "k"), ("L", "M"), ("N", "O"), ("P", "Q"))

# unpacking
alu, alu1, alu2, alu3 = tup5
print(alu)
print(alu1)
print(alu2)
print(alu3)

# tup6="g","h","i",("j","k"),("L","M"), ("N","O"), ("P","Q") #causes an error : too many values to unpack
#
# alu, alu1,alu2,alu3=tup6
# print(alu)
# print(alu1)
# print(alu2)
# print(alu3)

# causes an error : too many values to unpack
tup6 = "g", "h", "i", ("j", "k"), ("L", "M"), ("N", "O"), ("P", "Q")

alu, alu1, alu2, alu3, alu4, alu5, alu6 = tup6
print(alu)
print(alu1)
print(alu2)
print(alu3)
print(alu4)
print(alu5)
print(alu6)

# challange
print()
imelda = "More Mayham", "Imelda May", 2011, ((
    1, "Pulling the rug"), (2, "Psycho"), (3, "Mayham"), (4, "Kentish town waltz"))
print((imelda))

print()
a, b, c, d = imelda
print(a)
print(b)
print(c)
for i in d:
    print(" {}".format(i))

print()
a, b, c, d = imelda
print(a)
print(b)
print(c)
for i in d:
    x, y = i
    print("\tNo:{}, title:{}".format(x, y))
