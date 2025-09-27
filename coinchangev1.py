"""coinchange"""
def coinchange():
    """changing"""
    x = int(input())
    coin = 0
    coin += x//25
    x %= 25
    coin += x // 10
    x %= 10
    coin += x // 5
    x %= 5
    coin += x//1
    print(coin)
coinchange()
