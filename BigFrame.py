"""Big Frame"""
def main():
    """input"""
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    line5 = input()

    max_length = max(len(line1), len(line2), len(line3), len(line4), len(line5))
    
    
    print("*" * max_length)

    padding = " " * (max_length - len(line1))
    print(f"* {line1}{padding} *")

    padding = " " * (max_length - len(line2))
    print(f"* {line2}{padding} *")

    padding = " " * (max_length - len(line3))
    print(f"* {line3}{padding} *")

    padding = " " * (max_length - len(line4))
    print(f"* {line4}{padding} *")

    padding = " " * (max_length - len(line5))
    print(f"* {line5}{padding} *")

    print("*" * max_length)

main()
