""""right arrow"""
def main():
    """input"""
    k = int(input())
    n = int(input())

    mid = (n + 1) // 2

    for i in range(1, n + 1):
        num_spaces = abs(i - mid)
        num_stars = k
        
        print(" " * num_spaces + "*" * num_stars)

main()
 