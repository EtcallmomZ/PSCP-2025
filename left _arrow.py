"""left arrow"""
def main():
    """input"""
    k = int(input())
    n = int(input())
    result = ""

    for i in range(n):
        result += " " * (n-i)
        for j in range(1,k+1):
            if j == k:
                result += "*" + "\n"
            else:
                result += "*"

    print(result,end="")


main()
