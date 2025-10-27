""" try another code """
def rabbit():
    """ input """
    n = int(input())
    t_1 = []
    for _ in range(n):
        x = input().split(" ")
        t_1.append({
            "name":x[0],
            "weight":int(x[1])
        })

    sorted_rabbit = sorted(t_1,key = lambda x : x["weight"],reverse=True)
    max_rabbit = sorted_rabbit[0]
    count = 0
    for i in sorted_rabbit:
        if int(i["weight"]) > 15:
            count += 1

    print(count)
    print(max_rabbit['name'],max_rabbit['weight'])

rabbit()
