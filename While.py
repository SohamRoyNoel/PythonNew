# v = 0
# while v < 100:
#     print(" the no is {}".format(v))
#     v += 1

# direction = ["north", "south", "east", "west"]
# out = ""
# while out not in direction:
#     out = input("tell me the side you wanna get out : ")
# print("you're out")

import random
highest = 10

ans = random.randint(1, highest)
typed = int(input("enter yor guess : "))
while typed != ans:
    typed = int(input("enter yor guess : "))
    if typed != ans:
        print("try again later")
    else:
        print("now guessed correctly")
else:
    print("correct at first shot")
