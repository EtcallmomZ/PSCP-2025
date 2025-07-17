"""bubble tea"""
x = input()
y = input()

if "H" in x:
    x = x[2:]
    x = int(x)
    bubble_cal = x *5
elif "O" in x:
    x = x[2:]
    x = int(x)
    bubble_cal = x * 3
else:
    x = x[2:]
    x = int(x)
    bubble_cal = x * 2

if "R" in y:
    sweet_tea = y[2:3]
    tea_cc = y[4:]
    if sweet_tea == "1":
        tea_cal = int(tea_cc) *12
    elif sweet_tea == "2":
        tea_cal = int(tea_cc) *18
    else:
        tea_cal = int(tea_cc) *25

elif "T" in y:
    sweet_tea = y[2:3]
    tea_cc = y[4:]
    if sweet_tea == "1":
        tea_cal = int(tea_cc) * 15
    elif sweet_tea == "2":
        tea_cal = int(tea_cc) * 20
    else:
        tea_cal = int(tea_cc) * 30

else:
    sweet_tea = y[2:3]
    tea_cc = y[4:]
    if sweet_tea == "1":
        tea_cal = int(tea_cc) *10
    elif sweet_tea == "2":
        tea_cal = int(tea_cc) *15
    else:
        tea_cal = int(tea_cc) *20

print(tea_cal + bubble_cal)
