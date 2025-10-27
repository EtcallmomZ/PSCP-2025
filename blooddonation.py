""" blood donation """
AGE = int(input())
W = int(input())
COUNT = int(input())


if AGE == 17:
    consent = input().lower()
    if consent == "true" and W >= 45:
        print("Yes")
    else:
        print("No")
elif 60 <= AGE <= 70:
    docter = input().lower()
    if docter == "true" and W >= 45 and COUNT >= 1:
        print("Yes")
    else:
        print("No")
elif AGE > 70 or AGE < 17:
    print("No")
else:
    if AGE <= 55 and W >= 45:
        print("Yes")
    elif AGE > 55 and COUNT >= 1:
        print("Yes")
    else:
        print("No")
