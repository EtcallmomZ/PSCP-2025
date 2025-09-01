"""pickthem"""
import json
def main():
    """input"""
    x = input()
    x = json.loads(x)
    t = []
    result = ""
    for i in x:
        if not i%2:
            result += str(i)+ "\n"
            t.append(i)

    if not t:
        print("Nope")
    else:
        print(result,end="")
main()
