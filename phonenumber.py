"""phone number"""
def main():
    """input"""
    x = input()
    y = input()
    result = ""
    lenght = len(x)
    if lenght == 9:
        result += f"{x[0]} {x[1:5]} {x[5:]}"
    else:
        result += f"{x[0:2]} {x[2:6]} {x[6:]}"

    if y == "International":
        result = result.replace("0","+66",1)
        print(result)
    else:
        print(result)

main()
