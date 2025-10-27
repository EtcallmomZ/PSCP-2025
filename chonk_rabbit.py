"""hello"""
def main():
    """input"""
    n = int(input())
    name = []
    weight = []
    count = 0
    for _ in range(n):
        x = input()
        b = x.split()
        name.append(b[0])
        weight.append(int(b[1]))
        if int(b[1]) > 15:
            count += 1
    print(count)
    result = max(weight)
    name_rabbit = weight.index(result)
    print(name[name_rabbit],result)
main()
