"""coke"""
def main():
    """input"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if not b:
        print(a*d)
    elif not d:
        print(0)
    else:
        if not d%b:
            pro = (d // b) - 1
        else:
            pro = d//b

        common_coke = d - pro
        result = (pro*c) + (common_coke*a)
        print(result)

main()
