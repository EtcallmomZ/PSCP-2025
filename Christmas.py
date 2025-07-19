"""Christmas Light"""
def main():
    """input"""
    light = ("Red","Green","Blue")
    start = input()
    number = int(input())
    light = light*(number)
    if start == "R":
        my_list = light[0:number]
        print(" ".join(my_list))
    elif start == "G":
        my_list = light[1:number+1]
        print(" ".join(my_list))
    else:
        my_list = light[2:number+2]
        print(" ".join(my_list))
main()
