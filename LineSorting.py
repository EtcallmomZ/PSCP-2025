"""LineSorting"""
def main():
    """input"""
    n = int(input())
    t_1 = []
    for _ in range(n):
        x = input()
        t_1.append(x)

    t_1.sort(key=len)

    for i in t_1:
        print(i)
main()
