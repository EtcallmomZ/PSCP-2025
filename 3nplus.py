"""3nplus"""
def main():
    """input"""
    count = 0
    result = ""
    while True:
        x =  int(input())
        number = x
        if not x:
            break
        count += 1
        while number > 1:
            if not number%2:
                number /= 2
                count += 1
            else:
                number = number*3+1
                count += 1
        result += str(count) + "\n"
        count = 0

    print(result,end="")

main()
