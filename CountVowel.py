"""count vowel"""
def main():
    """input"""
    a = int(input())
    count = 0
    for _ in range(a):
        x = input()
        if x in ("A","E","I","O","U"):
            count += 1
        else:
            count += 0
    print(count)
main()
