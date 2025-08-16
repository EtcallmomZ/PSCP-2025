"""game"""
def main():
    """input"""
    a = int(input())
    b = int(input())

    win_a =  a//3
    win_b = b//3

    if a >= 3 and b >= 3:
        print(abs(win_a-win_b))
    elif a == 1 and b == 1:
        print(1)
    else:
        if a == 0 or b == 0:
            print(0)
        else:
            print("Error")

main()