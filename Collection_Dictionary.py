
dictionary = {
    "Ivy": "Soft sexy and round face",
    "Sreeparna": "Sharp sexy, good boobs",
    "Puja": "Flat, no boob, no heap",
    "Ankita": "Huge boobs and hips",
    "Amrita Mam": "Old is gold"
}
print(dictionary)

print(dictionary["Ivy"])


# adding a key and value:  INDEXERS ARE NOT USED

dictionary["Anneswa"] = "sexy dancer, dancing boobs"
print(dictionary)


# dictionary cant contain SAME KEY : instade it will update last one
dictionary["Puja"] = "Small butt, Chips boobs"
print(dictionary)


# deleting an item
del dictionary["Puja"]
print(dictionary)

del dictionary  # drops the entire dictionary, SO USE IT WITH key
print(dictionary)  # error bcz no dictionary exists

# REMOVE THE DICTIONARY ITEMS, but doesn't delete the dictionary
dictionary.clear()
print(dictionary)


# unexisting key in a dictionary causes error
print(dictionary["Sayani"])


# GETTING ITEM BY AN USER DEFINED KEY
while True:
    dick_key = input("enter the key please : ")
    if dick_key == "fuck":
        break
    discription = dictionary.get(dick_key)
    print(discription)

# it will never give an error if the key does't exists : it returns none


# if you need to JUSTIFY IF THE KEY EXIST OR NOT
while True:
    dick = input("enter the key")
    if dick == "duck":
        break
    if dick in dictionary:
        description = dictionary.get(dick)
        print(description)
    else:
        print("no key found {}".format(dick))


while True:
    dick = input("enter the key : ")
    if dick == "duck":
        break
    # 2nd is called default value
    description = dictionary.get(dick, "we don't have a slut named " + dick)
    print(description)


print()
# listing value instade of gettin them a list order
for i in dictionary:
    print(i)  # getting only the keys
print()
# getting the VALUES by KEY
for j in dictionary:
    print(dictionary[j])
print()
for k in dictionary:
    print(k)
    print(dictionary[k])


# ordering keys in dictionary
# dick_order_key=list(dictionary.keys())
# dick_order_key.sort()
# same but done under 1 line code
dick_order_key = sorted(list(dictionary.keys()))
for j in dick_order_key:
    print("Keys : {} || Values : {}".format(j, dictionary[j]))
print()
# another implementation of the same thing
for i in sorted(dictionary.keys()):
    print("Keys : {} || Values : {}".format(i, dictionary[i]))


print()
# getting key and values differently
for i in dictionary.keys():
    print(i)
for j in dictionary.values():
    print(j)


print(dictionary.items())

# getting tuple from dictionary
get_tup = tuple(dictionary.items())
print(get_tup)

# unpacking tuple:
for i in get_tup:
    x, y = i
    print("key : {} || value : {}".format(x, y))

# tuple -> dictionary
dicto = dict(get_tup)
print(dicto)

mylist = ["a", "b", "c", "d"]
listN = "abcdefghijklmnopqrstuvwxyz"
numbers = " 1234567890 "
empty = ""

empty = ",".join(listN)
print(empty)

nos_empty = ""
nos_empty = numbers.join(listN)
print(nos_empty)

# dictionaries cant be joined
print()
dictionary = {
    "Ivy": "Soft sexy and round face",
    "Sreeparna": "Sharp sexy, good boobs",
    "Puja": "Flat, no boob, no heap",
    "Ankita": "Huge boobs and hips",
    "Amrita Mam": "Old is gold"
}
dictionary1 = {
    "IvyN": "Soft sexy and round face",
    "SreeparnaN": "Sharp sexy, good boobs",
    "PujaN": "Flat, no boob, no heap",
    "AnkitaN": "Huge boobs and hips",
    "Amrita MamN": "Old is gold"
}
dictionart3 = dictionary.join(dictionary1)

dictionary = {
    "Ivy": "Soft sexy and round face",
    "Sreeparna": "Sharp sexy, good boobs",
    "Puja": "Flat, no boob, no heap",
    "Ankita": "Huge boobs and hips",
    "Amrita Mam": "Old is gold"
}

dictionary2 = {
    "nipple": "small and soft",
    "pussy": "little and wet",
    "boobs": "soft and heavy",
    "penus": "long and hard"
}

print(dictionary)
print()
print(dictionary2)


# updating combines two dictionaries, never returns a new dictionary
print()
dictionary.update(dictionary2)
print(dictionary)

print()
print(dictionary.update(dictionary2))  # update never returns a new dictionary

print()
# if you want to create a new dictionary then use COPY, rather than UPDATE
new_dictionary = dictionary.copy()
new_dictionary.update(dictionary2)
print(new_dictionary)

print()
print(dictionary2)
print(dictionary)  # is updated
