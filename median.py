"""eiweiw"""
def main():
    """input"""
    data = input().strip()
    numbers = [float(x) for x in data.split(", ")]
    numbers.sort()
    n = len(numbers)
    mid = n // 2

    if n % 2 == 1:
        median = numbers[mid]
    else:
        median = (numbers[mid - 1] + numbers[mid]) / 2

    print(f"{median:.2f}")

main()
