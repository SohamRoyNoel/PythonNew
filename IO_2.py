
poem = ["The Sick Rose\n"

        "BY WILLIAM BLAKE\n"

        "O Rose thou art sick.\n"
        "The invisible worm,\n"
        "That flies in the night\n"
        "In the howling storm:\n"

        "Has found out thy bed\n"
        "Of crimson joy:\n"
        "And his dark secret love\n"
        "Does thy life destroy.\n"]

# with open("E:\\Python Workspace\\Candy.txt", 'w') as candy:
#     for c in poem:
#         print(poem, file=candy)

# New word new line
# vit = input("enter the string : ")
# vit_2 = vit.split()
# with open("E:\\Python Workspace\\Candy.txt", 'w') as cat:
#     for i in vit_2:
#         print(i, file=cat)

# # since the speed of code is much much faster
# # than writing operation in, that is why
# # it is stored in a buffer, if the file size is too big
# # trying it using reading and writing a file parrelly

# with open("E:\\Python Workspace\\Candy.txt", 'r') as bull:
#     for i in bull:
#         print(i)

# print("*"*50)

# with open("E:\\Python Workspace\\Candy.txt", 'r') as bull:
#     for i in bull:
#         print(i, end="")

# print("*"*50)
# #.appand - strip : used to eleminate the string you want
# # cuts from beginning or end
# cit = []
# with open("E:\\Python Workspace\\Candy.txt", 'r') as bull:
#     for i in bull:
#         cit.append(i.strip('\n'))

# print(cit)
# for c in cit:
#     print(c)


# imelda = "More Mayham", "Imelda vy", "2011", ((
#     1, "Pullig the rug"), (2, "Psyco"), (3, "Mayham"), (4, "kentiz town worldx"))

# with open("E:\\Python Workspace\\Candy.txt", 'w') as bull:
#     print(imelda, file=bull)


# with open("E:\\Python Workspace\\Candy.txt", 'r') as tatti:
#     c = tatti.readline()

# im = eval(c)

# aut, alb, yr, trc = im
# print(aut)
# print(alb)
# print(yr)
# print(trc)

# ************************************************************************************************************
# More Mayham
# Imelda vy
# 2011
# ((1, 'Pullig the rug'), (2, 'Psyco'), (3, 'Mayham'), (4, 'kentiz town worldx'))
# ************************************************************************************************************


with open("E:\\Python Workspace\\Candy.txt", 'a') as Tatti:
    for i in range(1, 12):
        for j in range(1, 10):
            print("{} times {} is {}".format(i, j, i*j), file=Tatti)
