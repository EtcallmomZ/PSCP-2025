"""100meters"""
def main():
    """input"""
    number = 1
    result = ""
    for i in range(1,9):
        x = float(input())
        first = x
        second = x
        thrid = x
        if number < first:
            number = first
            result += str(i) + "\n"
        elif number < second:
            number = second
            result += str(i) + "\n"
        elif number < thrid:
            x = thrid
            result += str(i) + "\n"
        else:
            continue
    print(result)
main()
