"""Hamming"""
def main():
    """input"""
    x = input()
    y = input()
    count = 0

    lenght = len(x)
    for i in range (lenght):
        if x[i] != y [i]:
            count += 1

    print(count)
main()
