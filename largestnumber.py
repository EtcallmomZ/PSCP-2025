"""largestnumber"""
def main():
    """input"""
    x = int(input())
    y = int(input())
    z = int(input())
    x = str(x)
    y = str(y)
    z = str(z)
    number = [x+y+z,x+z+y,y+x+z,y+z+x,z+x+y,z+y+x]
    top = int(number[0])
    if int(number[1]) > top:
        top = int(number[1])
    if int(number[2]) > top:
        top = int(number[2])
    if int(number[3]) > top:
        top = int(number[3])
    if int(number[4]) > top:
        top = int(number[4])
    if int(number[5]) > top:
        top = int(number[5])

    print(top)

main()
