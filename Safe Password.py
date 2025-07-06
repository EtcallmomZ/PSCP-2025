"""Safe Password"""
def main():
    """blabla"""
    char = input()
    digit = int(input())

    if char == "H" and str(digit) == "4567":
        print("safe unlocked")
    elif char == "H":
        print("safe locked - change digit")
    elif str(digit) == "4567":
        print("safe locked - change char")
    else:
        print("safe locked")

main()
