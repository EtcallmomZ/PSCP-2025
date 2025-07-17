"""IT Business"""
def main():
    """input"""
    money_have = float(input())
    money_with = float(input())
    error = 0
    while True:
        x = input()
        if x == "end":
            break
        if "D" in x:
            x = x[2:]
            x = float(x)
            if money_with >= x:
                money_have += x
                money_with -= x
                error = 0
            else:
                error += 1
        elif "W" in x:
            x = x[2:]
            x = float(x)
            if money_have >= x:
                money_have -= x
                money_with += x
                error = 0
            else:
                error += 1
        else:
            error += 1

        if error == 3:
            break

    print(f"{money_have:.2f}")
    print(f"{money_with:.2f}")

main()
