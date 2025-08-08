"""backward"""
def main():
    """input"""
    result = []
    while True:
        x = input()
        if x == "NULL":
            break
        result.append(x)


    result = result[::-1]

    for i in result:
        print(i)
main()
