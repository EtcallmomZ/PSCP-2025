"""leapyear"""
def main():
    """input"""
    x = int(input())
    if  (not x % 4 and x % 100) or (not x % 400):
        print(f"{x} is a leap year.")
    else:
        print(f"{x} is not a leap year.")
main()
