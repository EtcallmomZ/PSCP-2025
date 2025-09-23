""" weight station """
def weight():
    """ input """
    x = float(input())
    n_1 = float(input())
    n_2 = float(input())
    n_3 = float(input())
    summary_before_add_n4 = n_1+ n_2+ n_3
    n_4 = abs(summary_before_add_n4 - (x*4))
    default = True
    avg_min = x / 2
    avg_max = avg_min + x
    if avg_min > n_1  or n_1 > avg_max:
        default = False
    if avg_min > n_2  or n_2 > avg_max:
        default = False
    if avg_min > n_3  or n_3 > avg_max:
        default = False
    if avg_min > n_4  or n_4 > avg_max:
        default = False
    summary_after_add_n4 = summary_before_add_n4 + n_4

    if summary_after_add_n4 > 15000:
        print("Overweight")
    elif default is False:
        print("Unbalance")
    elif summary_after_add_n4 > 15000 and default is False:
        print("Overweight")
    else:
        print("Pass",f"{n_4:.2f}")


weight()
