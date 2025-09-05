"""duplicate I"""
def main():
    """input"""
    m = int(input())
    n = int(input())
    t_1 = []
    t_2 = []
    t_3 = []
    for _ in range(m):
        x = int(input())
        t_1.append(x)
    for _ in range(n):
        y = int(input())
        t_2.append(y)

    for i in t_1:
        for g in t_2:
            if i == g:
                t_3.append(i)

    if not t_3:
        print("Nope")
    else:
        t_3.sort()
        for i in t_3[::-1]:
            print(i)

main()
