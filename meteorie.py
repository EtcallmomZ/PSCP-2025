"""meteorite"""
def main():
    """input"""
    a = float(input())
    b = int(input())
    c = float(input())

    if a < c or not a:
        print(0)
        return

    d = 0
    pow_b = 1

    while a >= c*pow_b:
        d += 1
        pow_b *= b

    missiles = (b**d-1)/(b-1)
    print(int(missiles))


main()
