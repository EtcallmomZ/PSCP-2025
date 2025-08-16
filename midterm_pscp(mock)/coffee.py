"""coffee"""
def main():
    """input"""
    a =  float(input())
    b =  float(input())
    c =  float(input())
    d =  float(input())
    e =  int(input())

    money_1 = a
    money_2 = 0
    discount_1 = a*(b/100)
    discount_2 = a*e
    price_after_discount_1 = a - discount_1
    price_after_discount_2 = c/100

    if e > 1:
        money_1 += price_after_discount_1*(e-1)
    else:
        money_1 = a


    if discount_2 >= d:
        money_2 = discount_2 - (discount_2 * price_after_discount_2)
    else:
        money_2 = discount_2


    if money_1 < money_2:
        print("1")
        print(f"{money_1:.2f}")
    elif money_1 == money_2:
        print("2")
        print(f"{money_2:.2f}")
    else:
        print("2")
        print(f"{money_2:.2f}")


main()
