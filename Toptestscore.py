"""Top Test Scorer"""
def main():
    """input"""
    a = int(input())
    count = 1
    top = -1
    for _ in range(a):
        x = int(input())
        if x > top:
            top = x
        elif x == top:
            count += 1
        else:
            continue
    print(top)
    print(count)
main()
