"""meteorite"""
def main():
    """input"""
    a = float(input())
    b = int(input())
    c = float(input())
    count = 1
    kg = a//b
    while kg >= c:
        kg //= b
        count += b
        

    print(count)

main()
