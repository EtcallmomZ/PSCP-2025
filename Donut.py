"""Donut"""
def main():
    """Donut"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if not d:
        print(0, 0)
        return

    if not c:
        print(a * d, d)
        return


    num_packages = d // (b + c)
    cost = num_packages * (a * b)
    donuts = num_packages * (b + c)


    remaining = d - donuts
    if remaining > 0:
        if remaining * a < a * b:
            cost += remaining * a
            donuts += remaining
        else:
            cost += a * b
            donuts += b + c

    print(cost, donuts)

main()
