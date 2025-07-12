"""pro"""
def main():
    """input"""
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())

    if z >= x:
        if not z % y:
            pro = z // x
            price = (y*a) * pro
            print(price)
        else:
            pro = z // x
            pro_2 = z % x
            price = ((y*a) * (pro))+ (pro_2*a)
            print(price)
    else:
        print(a*z)
main()
