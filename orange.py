"""orange"""
def main():
    """input"""
    a = int(input())
    b = int(input())
    tier = a

    for i in range(1,a+1):
        if i*i <= b:
            tier -= 1
            b -= i*i

    print(tier)
main()
