"""Last stand"""
import json
def main():
    """input"""
    x = input()
    x = json.loads(x)
    t = []
    for i in x:
        y = len(str(i))
        t.append(str(i)[y-1])

    for i in t:
        print(i)


main()
