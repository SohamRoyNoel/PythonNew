
tup = "a", "b", "c"
print(tup)

# tuple holds heterogenious items : like a movie tuple will not contain football
# lists are homogenious
porn = "Mia", "blue film", "2010"
porn2 = "Sunny", "blue film", "2001"
Male = "Sins", "White film", "2000"

print(porn2)
print(porn2[0])
print(porn2[1])
print(porn2[2])


porn2[0] = "Sunny Leeone"  # TUPLE IS IMMUTABLE : that cant be changed


# porn2[0]="Sunny Leeone" #TUPLE IS IMMUTABLE : that cant be changed

porn2 = porn2[0], "brown film", porn2[2]
print(porn2)

# case of list rather tuple
porn2a = ["porn", "dick", "pussy"]
print((porn2a))
porn2a[0] = "BOOBS"
print(porn2a)  # LISTS ARS MUTABLE : can be changed easyly


# unpacking the tuple
Name, type, year = porn  # executes right to left
print(Name)
print(type)
print(year)
