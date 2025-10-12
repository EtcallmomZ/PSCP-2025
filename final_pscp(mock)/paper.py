""" paper """
def paper():
    """input"""
    x = input()
    y = input()

    start = int(y[1:])-int(x[1:])
    result = 1

    for _ in range(start):
        result *= 2

    print(result)


paper()
