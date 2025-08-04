"""Cyan's password generator"""
def main():
    """input"""
    x = input()
    y = input()
    z = input()

    x_len = len(x)
    y_len = len(y)

    if x_len >= 5 and y_len >= 5:
        password = x[0:2] + y[len(y) - 1] + str(z)[len(z)-1]
        print(password)
    else:
        password = x[0] + str(z) + y[len(y) - 1]
        print(password)

main()
