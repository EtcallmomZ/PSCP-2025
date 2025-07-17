"""heads and legs"""
def main():
    """input"""
    a = int(input())
    b = int(input())

    rabbit = (b-2 * a) // 2
    bird = a - rabbit

    if rabbit >= 0 and bird >= 0 and (2*bird + 4*rabbit == b):
        print(rabbit, bird)
    else:
        print("Impossible")

main()
