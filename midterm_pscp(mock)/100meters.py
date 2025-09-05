"""100meters"""
def main():
    """input"""
    result = ""
    x = float(input())
    first = x
    for i in range(8):
        y = float(input())
        number = y
        second = y
        thrid = y
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
