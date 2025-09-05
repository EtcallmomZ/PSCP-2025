"""FOR!F-Ball"""
def main():
    """input"""
    x = input()
    ball = 1
    for i in x:
        if i ==  "A":
            if ball == 1:
                ball = 2
            elif ball == 2:
                ball = 1
        if i == "B":
            if ball == 2:
                ball = 3
            elif ball == 3:
                ball = 2
        if i == "C":
            if ball == 1:
                ball = 3
            elif ball == 3:
                ball = 1
    print(ball)
main()
