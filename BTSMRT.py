"""BTSMRT"""

def main():
    '''bts mrt'''
    x = input()
    y = float(input())
    z = float(input())

    if x == "Children Day":
        if (y < 14) and (z <= 140):
            print("FREE")
        else:
            print("PAY")
    elif x == "Senior Day":
        if y >= 60 or ((y < 14 )and (z < 90)):
            print("FREE")
        else:
            print("PAY")
    else:
        if( y < 14) and (z < 90):
            print("FREE")
        else:
            print("PAY")
main()
