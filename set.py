""" difference """
def difference():
    """ input """
    n = int(input())
    t_1 = []
    m = int(input())
    t_2 = []
    for _ in range(n):
        x = int(input())
        t_1.append(x)

    for _ in range(m):
        y = int(input())
        t_2.append(y)

    set_1 = set(t_1)
    set_2 = set(t_2)

    print(*sorted(set_1 - set_2))


difference()
