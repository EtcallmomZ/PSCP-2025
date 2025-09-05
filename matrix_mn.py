"""Matrix_MN"""
def main():
    """input"""
    m = int(input())
    n = int(input())
    for  _ in range(m):
        tmp = []
        for _ in range(n):
            tmp.append(input())
        print(" ".join(tmp))
main()
