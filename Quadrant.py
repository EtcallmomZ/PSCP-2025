"""Quadrant"""
def main():
    """input"""
    x = int(input())
    y = int(input())

    if x > 0 and y > 0:
        print("Q1")
    elif x < 0 < y:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    elif not x and not y:
        print("O")
    elif not y:
        print("X")
    elif not x:
        print("Y")
    else:
        print("Q4")
main()
