"""calculator"""
def main():
    """input"""
    x = int(input())
    count = ""

    for i in range(1,x+1):
        if x == 1:
            count += str(i)
            break
        if i == x:
            count += str(i) + "="
        else:
            count += str(i) + "+"
    print(len(count))
main()
