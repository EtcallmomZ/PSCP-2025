"""seven"""
def main():
    """input"""
    x = int (input())
    num = (1,7,9,3)
    if not x % 4:
        print(num[0])
    elif x % 4 == 1:
        print(num[1])
    elif x % 4 == 2:
        print(num[2])
    else:
        print(num[3])
main()
