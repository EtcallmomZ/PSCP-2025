"""RuleofThree"""
def main():
    """input"""
    x = int(input())
    price_list = []
    size_list = []

    for _ in range(x):
        price = float(input())
        size = float(input())
        price_list.append(price)
        size_list.append(size)

    best_value = -1
    best_index = -1

    for i in range(x):
        value = size_list[i] / price_list[i]
        if value > best_value:
            best_value = value
            best_index = i
        elif value == best_value:
            if price_list[i] < price_list[best_index]:
                best_index = i

    print(f"{price_list[best_index]:.2f}", f"{size_list[best_index]:.2f}")

main()
