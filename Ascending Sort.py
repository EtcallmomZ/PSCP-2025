"""Ascending Sort"""
def main():
    """input"""
    n = int(input())
    number = []

    for _ in range(n):
        x = int(input())
        number.append(x)
        number.sort()

    for i in number:
        print(i)

main()
