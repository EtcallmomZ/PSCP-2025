"""season"""

x = int(input())
y = int(input())

season = ["winter","spring","summer","fall"]

if x in (1,2):
    print(season[0])
elif x == 3:
    if y < 21:
        print(season[0])
    else:
        print(season[1])
elif x in (4,5):
    print(season[1])
elif x == 6:
    if y < 21:
        print(season[1])
    else:
        print(season[2])
elif x in (7,8):
    print(season[2])
elif x == 9:
    if y < 21:
        print(season[2])
    else:
        print(season[3])
elif x in (10,11):
    print(season[3])

else:
    if y < 21:
        print(season[3])
    else:
        print(season[0])
