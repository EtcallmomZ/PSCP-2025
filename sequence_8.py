""" sequence 8 """
def print_simple_triangle(rows):
    """input"""
    for i in range(1, rows + 1):
        leading_spaces = "   " * (rows - i)

        line_parts = [f"{j:02d}" for j in range(1, i + 1)]
        line_content = " ".join(line_parts)

        print(leading_spaces + line_content)


print_simple_triangle(int(input()))
