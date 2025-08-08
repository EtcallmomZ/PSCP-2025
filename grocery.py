"""Grocery"""
def main():
    """input"""
    x = input()
    x = x.split()
    price = []
    price.extend(x)
    result = int(price[0]) * 10 + int(price[1]) * 25 + int(price[2])*3
    print(result)

main()
