""" dinity"""
def dinity():
    """input"""
    while True:
        x = input()
        if x == "0":
            break
        while True:
            result = 0
            if len(x) == 1:
                break
            for i in x:
                result += int(i)
            x = str(result)
        print(x)
dinity()
