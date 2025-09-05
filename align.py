"""align"""
def main():
    """input"""
    size = int(input())
    way = input()
    text = input()

    way = way.lower()
    if way == "left":
        print(text.ljust(size))
    elif way == "right":
        print(text.rjust(size))
    else:
        print(text.center(size))

main()
