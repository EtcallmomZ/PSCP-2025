"""Kangaroo"""
def main():
    """input"""
    a = int(input())
    b = int(input())
    c = int(input())
    first = b - a
    second = c - b

    print(max(first,second) -1 )
main()
