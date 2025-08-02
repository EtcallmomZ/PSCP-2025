"""FiveX"""
def main():
    """input"""
    x = int(input())
    result = ""
    for i in range(1,x+1):
        if not i%5:
            result += "X"
        else:
            result += "*"

    print(result)




main()
