""" tictactoe """
def tictactoe():
    """ input """
    line1 = input()
    line2 = input()
    line3 = input()

    col1 = line1[0]+line2[0]+line3[0]
    col2 = line1[1]+line2[1]+line3[1]
    col3 = line1[2]+line2[2]+line3[2]

    cross1 = line1[0]+line2[1]+line3[2]
    cross2 = line1[2]+line2[1]+line3[0]

    if "XXX" in (line1,line2,line3,col1,col2,col3,cross1,cross2):
        print("X WIN")
    elif "OOO" in (line1,line2,line3,col1,col2,col3,cross1,cross2):
        print("O WIN")
    else:
        print("DRAW")
tictactoe()
