"""gcd_V2"""
def gcd():
    """gcd without using math.gcd()"""
    x = float(input())
    y = float(input())

    while y:
        x,y = y,x%y

    print(int(abs(x)))

gcd()
