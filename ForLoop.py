for i in range(1, 20):
    print("the number is {0:4}".format(i))

number = "9,151,858,141,259,145,148,852,123"
for i in range(0, len(number)):  # default it can take 0 to n-1 - Extracts each number from element
    print(number[i])

number = "9,151,858,141,259,145,148,852,123"
for i in range(0, len(number)):
    if number[i] in "123456789":
        print(number[i])

number = "9,151,858,141,259,145,148,852,123"
for i in range(0, len(number)):
    if number[i] in "123456789":
        print(number[i], end="")

number = "9,151,858,141,259,145,148,852,123"
for i in range(0, len(number)):
    if number[i] in "123456789":
        # violates the commas case
        print("the number is {0}".format(number[i], end=""))

number = "9,151,858,141,259,145,148,852,123"
cont = " "
for i in range(0, len(number)):
    if number[i] in "123456789":
        cont = cont+number[i]

print("the number is {0}" .format(cont))


number = "9,151,858,141,259,145,148,852,123"
for i in range(0, len(number)):
    if number[i] in "123456789":
        if(number[i] == "1"):
            print(number[i] + "- One")
        elif(number[i] == "2"):
            print(number[i] + "- Two")
        elif (number[i] == "3"):
            print(number[i] + "- Three")
        elif (number[i] == "4"):
            print(number[i] + "- Four")
        elif (number[i] == "5"):
            print(number[i] + "- Five")
        elif (number[i] == "6"):
            print(number[i] + "- Six")
        elif (number[i] == "7"):
            print(number[i] + "- Seven")
        elif (number[i] == "8"):
            print(number[i] + "- Eight")
        elif (number[i] == "9"):
            print(number[i] + "- Nine")

for prog in ["Java", "C#", "Python", "C++", "C", "JavaScript"]:
    print("the best is {0}" .format(prog))


# Multiplication table
for i in range(1, 12):
    for j in range(1, 12):
        print("{0} times {1} is {2}".format(i, j, i*j))
    print("")

# Triangle
for i in range(0, 6):
    for j in range(0, i):
        print("*", end="")
    print()

# reverse triangle
for i in range(6, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()

# isoscale triangle
for i in range(0, 6):
    for j in range(0, i):
        print("*", end="")
    print()
for i in range(6, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()

for i in range(0, 6):
    for j in range(0, i):
        print("*", end="")
    print()
