""" prime number """
def prime():
    """ input """
    x = int(input())
    last_number = int(x**0.5)
    if x == 1:
        print("NO")
        return
    if x == 2:
        print("YES")
        return
    if not x%2:
        print("NO")
        return

    for i in range(3,last_number+1,2):
        if not x % i:
            print("NO")
            return
    print("YES")

prime()
