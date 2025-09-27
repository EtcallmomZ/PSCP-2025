"""Donut"""
def main():
    """input"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if not c:
        print(a*d)
    elif not d:
        print(0,0)

    else:
        pro = d//b
        price = d - pro
        donut = (pro*c) + price
        result = price*a
        print(result,donut)


main()
