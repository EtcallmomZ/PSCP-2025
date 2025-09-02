"""Gift II"""
def main():
    """input"""
    t = []
    G_1 = int(input())
    t.append(G_1)
    G_2 = int(input())
    t.append(G_2)
    G_3 = int(input())
    t.append(G_3)
    G_4 = int(input())
    t.append(G_4)
    G_5 = int(input())
    t.append(G_5)
    G_6 = int(input())
    t.append(G_6)
    G_7 = int(input())
    t.append(G_7)
    G_8 = int(input())
    t.append(G_8)


    number_2 = ""

    if not t[0]%2:
        number_2 = t[0]
    if not t[1]%2:
        number_2 = t[1]
    if not t[2]%2:
        number_2 = t[2]
    if not t[3]%2:
        number_2 = t[3]
    if not t[4]%2:
        number_2 = t[4]
    if not t[5]%2:
        number_2 = t[5]
    if not t[6]%2:
        number_2 = t[6]
    if not t[7]%2:
        number_2 = t[7]

    print(number_2)

main()
