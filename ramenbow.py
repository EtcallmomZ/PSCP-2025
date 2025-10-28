""" ramen bowl """
def ramen():
    """ input """
    n = int(input())
    t_1 = []
    t_2 = []
    count = 0
    for _ in range(n):
        x = int(input())
        if x not in t_1:
            t_1.append(x)
        else:
            t_2.append(x)
    
    print(t_1)
    print(t_2)




ramen()
