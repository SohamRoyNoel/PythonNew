name = input("Enter your name ? ")
age = int(input("How old are you " + name))
print("{0}, you are {1} years old" .format(name, age))

if age > 18:
    print("you're enough")
else:
    print("/you're not enough")

age = int(input("What is your age : "))
name = input("Enter name : ")
if age > 18:
    print("come and have fun")
    v = input("Wanna continue? press y/n :")
    if v == "y":
        vv = int(input("guess a number : "))
        if vv < 10:
            if vv == 6:
                print("{0} You've done" .format(name))
            else:
                print("try again later {0}".format(name))
        elif vv > 10:
            print("choose a lower no")
            p1 = int(input("choose again"))
            if p1 == 6:
                print("{0} Youve done" .format(name))
            else:
                print("Try again later {0}" .format(name))
    else:
        print("Good bye {0}" .format(name))
else:
    print("{0} come {1} years later".format(name, 18-age))
