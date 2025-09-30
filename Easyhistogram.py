""" Easy histogram """
def main():
    """ input """
    x = input()
    t_1 = {}

    for i in x:
        if i.isalpha():
            t_1[i] = t_1.get(i, 0) + 1

    for g in range(ord("a"), ord("z") + 1):
        lower = chr(g)
        upper = chr(g).upper()
        if lower in t_1:
            print(f"{lower} = {t_1[lower]}")
        if upper in t_1:
            print(f"{upper} = {t_1[upper]}")

main()
