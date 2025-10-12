""" least vowel """
def least():
    """ input """
    t_1 = ["a","e","i","o","u"]
    x = input().lower().split()
    long = len(x)
    t_2 = []
    t_3 = []
    count = 0
    for i in range(long-1):
        for j in x[i]:
            if j in t_1:
                count += 1
                if j == x[i[-1]]:
                    t_2.append(x[1])
                    t_3.append(count)



    print(t_2)



least()
