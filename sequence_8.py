"""sequence 8"""
def main():
    """input"""
    n = int(input())
    count = 0
    result = ""
    for i in range(n):
        i = 1
        count += 1
        result += " " * (n-count)
        for j in range(i,count+1):
            if j == count:
                result += f"0{j}" + "\n"
            else:
                result += f"0{j}" + " "

    print(result,end = "")


main()
