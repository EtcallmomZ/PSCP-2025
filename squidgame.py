"""Squid Game 3 - Tug-of-War"""
def main():
    """bla bla bla"""
    count_a = 0
    count_b = 0
    for i in range(1,21):
        x = int(input())
        if i <= 10:
            count_a += x
        else:
            count_b += x

    if count_b > count_a :
        print("A")
    elif count_a == count_b:
        print("AB")
    else:
        print("B")
main()
