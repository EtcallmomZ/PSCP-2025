"""sequence 5"""
def main():
    """input"""
    n = int(input())
    count = 0
    result = ""
    for i in range(n,0,-1):
        if count == 7-1:
            result += str(i) + "\n"
            count = 0
        else:
            result += str(i) + " "
            count += 1

    print(result,end="")

main()
