age = 25
# print("My age is" + age)

print("My age is {0}", format(age))
print("My age {0} is" .format(age))
# print("My age is {0}", .format(age))

print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6}" .format(
    31, "January", "March", "April", "May", "June", "July"))

print()

print("""January = {2}
February= {0}
March ={1}
April = {2}
May ={1}
June = {2}
July ={1}
august= {2}
september ={1}
october= {2}
november ={1}
december = {2}""" .format(28, 30, 31))

# in python 2

print()

print("I am %d years old" % age)

print("Pi is approx {0}" .format(22/7))

print()

for i in range(1, 12):
    print("no is {0} sq = {1} cube = {2}".format(
        i, i**2, i**3))  # in indentation

print()

for i in range(1, 12):
    # second parameter is called WIDTH (right indent)
    print("no is {0:2} sq = {1:4} cube = {2:4}".format(i, i**2, i**3))

print()

for i in range(1, 12):
    # < stands for LEFT side WILL be equal indent
    print("no is {0:<2} sq = {1:<4} cube = {2:<4}".format(i, i**2, i**3))

print()

for i in range(1, 12):
    print("no is {} sq = {0} cube = {:4}".format(i, i**2, i**3))
