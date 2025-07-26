"""Ball"""
def main():
    """input"""
    x = float(input())
    count = 0
    if x <= 0.01:
        count = 0

    while x > 0.01:
        x = x*3/5
        if x > 0.01:
            count += 1
        else:
            break

    print(count)
main()
