""" one for all """
def one():
    """ input """
    n = int(input())
    result = ""
    for i in range(1,n+1):
        x =  input()
        if i == n:
            result += x + f"_{i}"
        elif not i%2:
            result += x + "-" * i
        else:
            result += x + "*" * i

    print(result)

one()
