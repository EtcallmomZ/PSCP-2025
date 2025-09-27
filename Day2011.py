"""a"""

def main():
    """a"""
    day = int(input())
    month = int(input())

    day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day_passed = day - 1

    for i in range(month - 1):
        day_passed += day_in_month[i]

    day_dict = {0:"Saturday", 1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday",
                6:"Friday"}

    print(day_dict.get(day_passed % 7))

main()
