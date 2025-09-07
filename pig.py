"""Pig"""
def pig():
    """input"""
    n = int(input())
    t_1 = input().split(" ")
    t_1 = list(map(int, t_1))

    t_2 = []
    max_number = []

    for i in range(n):
        number = (t_1[2*i], t_1[2*i+1])
        t_2.append(number)
        max_number.append(max(number))

    if len(t_2) == 1:
        print(max_number[0])
    else:
        result = " + ".join(map(str, max_number))
        result += f" = {sum(max_number)}"
        print(result)

pig()
