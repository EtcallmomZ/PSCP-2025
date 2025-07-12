"""sum of number"""
def main():
    """input"""
    x = int(input())
    result = 0
    while True:
        if result == x:
            break
        y = int(input())
        if y == -1:
            break
        result += y
    print(result)

main()
