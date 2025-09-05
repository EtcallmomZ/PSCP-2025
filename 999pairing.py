"""999pairing"""
def main():
    """input"""
    n = int(input())
    x = input()
    y = input()
    count = 0
    for i in range(n):
        if int(x[i]) + int(y[i]) == 9:
            count += 1

    if count == n:
        print("YES")
    else:
        print(f"NO {n-count}")
main()
