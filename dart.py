""" dart """
def dart():
    """ input """
    n = int(input())
    score = 0
    for _ in range(n):
        t_1 = input().split()
        area = (int(t_1[0])**2 + int(t_1[1])**2)**0.5
        if area <= 2:
            score += 5
        elif area <= 4:
            score += 4
        elif area <= 6:
            score += 3
        elif area <= 8:
            score += 2
        elif area <= 10:
            score += 1
        else:
            score += 0
    print(score)
dart()
