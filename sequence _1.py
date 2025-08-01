"""sequence I"""
def main():
    """input"""
    m = int(input())
    n = int(input())
    all_num = m*n
    result = ""

    for i in range(1,all_num+1):
        if i == n or not i%n:
            result += str(i) + "\n"
        else:
            result += str(i) + " "

    print(result,end="")


main()
