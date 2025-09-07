"""word sequence"""
def main():
    """input"""
    n = input()
    long_text = len(n)
    for i in range(1,long_text+1):
        print(n[:i])
main()
