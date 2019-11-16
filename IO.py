
file = open("E:\\Python Workspace\\ReadIO.txt", "r")
for line in file:
    print(line)
file.close()

print("*************************************************************************")

file = open("E:\\Python Workspace\\ReadIO.txt", "r")
for line in file:
    if "wish" in line.lower():
        print(line)
file.close()

print("*************************************************************************")

file = open("E:\\Python Workspace\\ReadIO.txt", "r")
for line in file:
    print(line, end="")
file.close()

print("*************************************************************************")

with open("E:\\Python Workspace\\ReadIO.txt", "r") as bull:
    for i in bull:
        if "wish" in i:
            print(i)

print("*************************************************************************")

with open("E:\\Python Workspace\\ReadIO.txt", "r") as bull:
    line = bull.readline()
    while line:
        print(line, end="")
        line = bull.readline()

print("*************************************************************************")

# converts into list
with open("E:\\Python Workspace\\ReadIO.txt", "r") as bull:
    line2 = bull.readlines()
print(line2)
# #after every line a \n comes, that amkes no sence

print("*************************************************************************")

with open("E:\\Python Workspace\\ReadIO.txt", "r") as bull:
    # line=bull.readlines()
    for i in bull.readlines()[::-1]:  # reverse order of line
        print(i, end="")

print("*************************************************************************")

# Reverse the element of the file
with open("E:\\Python Workspace\\ReadIO.txt", "r") as bull:
    # line=bull.readlines()
    for i in bull.read()[::-1]:  # reverse order of each line and word
        print(i, end="")

print("*************************************************************************")
