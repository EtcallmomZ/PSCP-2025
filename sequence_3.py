"""sequence_3"""
def main():
    """input"""
    n = int(input())
    first_n = n
    result = ""
    count = 0
    for i in range(2,n+2):
        for j in range(i,n+2,1):
            if count == first_n -1:
                result += str(j) + "\n"
                count = 0
            else:
                result += str(j) + " "
                count += 1

        n += 1
    print(result,end="")
main()
