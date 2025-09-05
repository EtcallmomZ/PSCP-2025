"""Donut"""
import math
def main():
    """input"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    pro = math.ceil(d/(b+c))
    cost = pro*b*a
    donut = pro*(b+c)
    print(cost,donut)


main()
