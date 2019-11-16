parrot = "parrot is a sucker"
print(parrot)
print(parrot[1])
print(parrot[0])
print(parrot[6])  # space
print(parrot[-1])
print(parrot[0:2])
print(parrot[0:8])
print(parrot[3:9])
print(parrot[-2:0])  # nothing comes after the last letter
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:-1])  # starts @ -1 (r) & runs -4 from right
print(parrot[0:6:2])  # counts 6 chars from LEFT, skips 2
print(parrot[0:6:3])

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
print(numbers[0::3])  # it removes 0 at the last 1
print(numbers[0::4])

str1 = "Soham"
str2 = " loves"
str3 = " Ivy, Sriparna Khamrui, Sriparna Guha Roy, Ankita Nath, Amrita mam"
print(str1 + str2 + str3)

# string multiplication
print((str1+str2+str3)*2)

# print((str1+str2+str3)*2 + 4) # OPERATOR PRESIDENCE error

print((str1+str2+str3)*(2 + 4))

today = "monday"
print("day" in today)
print("fri" in today)
print("parrot" in "parrot")
print("parrot" in today)
