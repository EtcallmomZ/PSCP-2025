"""sequence_4"""
def main():
    """input"""
    n = int(input())
    result = ""
    for i in range(1,n*n+1,n):
        for j in range(i,i+n):
            if not j%n:
                result += str(j) + "\n"
            else:
                result += str(j) + " "

    print(result,end="")
main()
