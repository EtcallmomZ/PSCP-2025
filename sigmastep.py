"""sigmastep"""
def main():
    """input"""
    x = int(input())
    y = int(input())
    n = int(input())
    total = 0
    if x == y:
        print(x)
    elif x < y and n >= 1:
        for i in range(x,y+1,n):
            total += i
        print(total)
    elif x > y and n < 0:
        for i in range(x,y-1,n):
            total += i
        print(total)
    else:
        print("error")

main()
