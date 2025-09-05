"""missingnumber"""
def main():
    """input"""
    n = int(input())
    t_1 = []
    t_2 = []
    while True:
        x = int(input())
        if not x:
            break
        t_1.append(x)

    t_1.sort()
    for i in range(1,n+1):
        if i not in t_1:
            t_2.append(i)
    t_2.sort()
    for i in t_2:
        print(i)

main()
