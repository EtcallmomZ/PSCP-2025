"""Retangle area"""
def retangle():
    """ input """
    a = input().split()
    b = input().split()
    widht = min(int(a[0]) + int(b[2]),int(b[0]) + int(b[2])) - max(int(a[0]),int(b[0]))
    height = min(int(a[1]) + int(a[3]),int(b[1])+int(b[3])) - max(int(a[1]),int(b[1]))
    area = max(0,widht)*max(0,height)

    if not area:
        print("no overlapping")
    else:
        print(int(area))
retangle()
