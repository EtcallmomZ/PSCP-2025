""" olympic """
def olympic():
    """ input """
    n = int(input())
    t_1 = []
    rank = 1
    for _ in range(n):
        info = input().split(" ")
        t_1.append({
            "country":info[0],
            "gold" : int(info[1]),
            "silver" : int(info[2]),
            "bronze" : int(info[3]),
            "total": int(info[1])+int(info[2]) + int(info[3]) 
        })

    result = sorted(t_1, key = lambda x: (-x["gold"],-x["silver"],-x["bronze"],x["country"]))
    previous = (None,None,None)
    for i,j in enumerate(result,start=1):
        current = (j["gold"],j["silver"],j["bronze"])
        if current != previous:
            rank = i
        print(rank,j['country'],j['gold'],j['silver'],j['bronze'],j['total'])
        previous = current
olympic()
