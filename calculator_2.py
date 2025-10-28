""" calculator2 """
def calculator():
    """ input """
    n = int(input())
    if n == 1:
        print(1)
    else:
        l = len(str(n))

        result = 0

        for i in range(1,l):
            count  = 9 *(10**i-1)
            result += count * i

        start = 10**(l-1)
        count = n - start + 1
        result += count * l

        print(result+n)


calculator()
