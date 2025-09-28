"""Big Frame"""
def main():
    """input"""
    line1 = input().strip()
    line2 = input().strip()
    line3 = input().strip()
    line4 = input().strip()
    line5 = input().strip()

    max_len = max(len(line1), len(line2), len(line3), len(line4), len(line5))
    frame_width = max_len + 4

    print("*" * frame_width)
    print(f"* {line1.ljust(max_len)} *")
    print(f"* {line2.ljust(max_len)} *")
    print(f"* {line3.ljust(max_len)} *")
    print(f"* {line4.ljust(max_len)} *")
    print(f"* {line5.ljust(max_len)} *")
    print("*" * frame_width)
main()
