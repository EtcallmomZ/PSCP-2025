"""run lenght encoding"""
def main():
    """input"""
    x = input()
    count = 0
    text = x[0]
    result = ""
    for i in x:
        if i == text:
            count += 1
        else:
            result += f"{count}{text}"
            count = 1
            text = i
    result += f"{count}{text}"
    print(result)


main()
