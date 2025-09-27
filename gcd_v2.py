"""gcd_V2"""
def gcd():
    """gcd without using math.gcd()"""
    t_1 = []
    x = float(input())
    t_1.append(int(x))
    y = float(input())
    t_1.append(int(y))

    min_num = min(t_1)
    result = 0
    for i in range(min_num,0,-1):
        if (not t_1[0] %i ) and (not t_1[1] %i):
            result = i
            break

    print(result)

gcd()
