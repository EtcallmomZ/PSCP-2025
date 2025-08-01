"""sequence 7"""
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

    for k in range(n):
        k = 1
        count -= 1
        for l in range(k,count+1):
            if l == count:
                result += str(l) + "\n"
            else:
                result += str(l) + " "

    print(result,end="")

main()
