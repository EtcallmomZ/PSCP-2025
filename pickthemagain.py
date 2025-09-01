"""pickthemagain"""
def main():
    """input"""
    x = input()
    x = x.split()
    t = []

    for i in x:
        if not int(i) %3 or not int(i)%5:
            t.append(i)

    if not t:
        print("Nope")
    else:
        for i in t[::-1]:
            print(i)

main()
