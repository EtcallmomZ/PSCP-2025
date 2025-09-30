"""inflation"""
def inflation():
    """ input """
    n = int(float(input())*100)
    k = int(input())

    for _ in range(k):
        n = (n*10381)//10000
    a = n%100
    n //= 100
    print(f"{n}.{a:02}")
inflation()
