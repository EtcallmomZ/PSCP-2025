"""sequence II"""
def main():
    """input"""
    n = int(input())
    result = ""
    count = 0
    for i in range(0,n):
        for j in range(i,n*n,n):
            if count == n-1:
                result += str(j) + "\n"
                count = 0
            else:
                result += str(j) + " "
                count += 1


    print(result,end="")






main()
