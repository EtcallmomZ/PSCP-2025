"""sequence 6"""
def main():
    """input"""
    n = int(input())
    count = 0
    result = ""
    for i in range(n):
        i = 1
        count += 1
        for j in range(i,count+1):
            if j == count:
                result += str(j) + "\n"
            else:
                result += str(j) + " "
    print(result,end="")

main()
