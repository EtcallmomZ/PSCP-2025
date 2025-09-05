"""median"""

def main():
    """input"""
    x = input()
    x = x.split(",")
    print(type(x))
    result = 0
    if not len(x)%2:
        number = x.sorted(x)
        print(number)
        mean_1 = len(x) / 2
        mean_2 = mean_1 + 1
        result = mean_1 + mean_2
    else:
        number = x.sorted(x)
        lenght = len(x) / 2
        result = number[int(lenght)]

    print(f"{result:.2f}")

main()
