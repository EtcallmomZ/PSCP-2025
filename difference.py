""" difference """
import json
def main():
    """ difference """
    a = input()
    b = input()
    a = json.loads(a)
    b = json.loads(b)
    for i in a:
        if i in b:
            b.remove(i)
            a.remove(i)
    for i in b:
        if i in a:
            b.remove(i)
            a.remove(i)
    
    if not a and not b:
        print("ONAJI DAYO!")
    else:
        before_list = min(a,b)
        after_list = max(a,b)
        print(before_list[0],len(before_list))
        print(after_list[0],len(after_list))

main()