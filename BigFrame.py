"""Big Frame"""
def main():
    """input"""
    result = ""
    for _ in range(5):
        x = input()
        result +=  x + "\n"


    long = len(x) + 2
    print("*" * long)
    print(result,end="")
    print("*" * long)

main()
