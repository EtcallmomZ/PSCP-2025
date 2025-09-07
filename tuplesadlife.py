"""tuple sad life"""
def main():
    """tuple sad life"""
    x = str(input())
    y = str(input())
    x = x.split(" ")
    t_1 = tuple(x)
    n = t_1.count(y)
    where_is_it = t_1.index(y)
    for _ in range(n):
        print(" ".join([str(where_is_it)]*n))
main()
