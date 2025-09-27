"""align"""
def main():
    """input"""
    size = int(input())
    align_type = input().lower()
    text = input()
    if align_type == "left":
        print(text.ljust(size))
    elif align_type == "right":
        print(text.rjust(size))
    else:
        padding_total = size - len(text)
        padding_left = (padding_total + 1) // 2
        padding_right = padding_total - padding_left
        left_spaces = " " * padding_left
        right_spaces = " " * padding_right
        print(f"{left_spaces}{text}{right_spaces}")

main()
