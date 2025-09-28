""""right arrow"""
def main():
    """input"""
    k = int(input())
    n = int(input())


    for i in range(n//2 + 1):
        print(" " * i + "*" * k)

    for i in range(n//2 -1 ,-1,-1):
        print(" " * i + "*" * k)

main()
