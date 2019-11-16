
dec = range(0, 100)
new_dec = dec[0:10:2]
print(new_dec == range(0, 10, 2))

print(range(0, 5, 2) == range(0, 6, 2))  # contains same

vol = range(0, 5, 2)
vol_1 = range(0, 5, 2)

for i in vol:
    print(i)
print()
for i in vol_1:
    print(i)


rev = range(0, 10)
new_rev = rev[0:10:-2]
print(list(new_rev))  # nothing will be printed bcz
# WE NEED TO REVERSE THE ITEMS TO GET IT

rev_2 = range(0, 10)
new_rev_2 = rev_2[10:0:-2]
print(list(new_rev_2))


backstring = "egaugnal taerg a si nohtyp"
print(backstring[::-1])
