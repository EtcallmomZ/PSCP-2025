""" sq """
def main():
    """ input """
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        is_ok = True

        b = 2
        while b * b <= i:
            if not i % (b * b):
                is_ok = False
                break
            b += 1

        if is_ok:
            count += 1
    print(count)
main()
