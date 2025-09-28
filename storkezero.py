""" stroke zero """
def zero():
    """ input """
    n = int(input())

    for i in range(1, n + 1):
        row_numbers = []
        for j in range(1, i + 1):
            if i == n or j == 1 or j == i:
                row_numbers.append("0")
            else:
                row_numbers.append("1")

        print(" ".join(row_numbers))

zero()
