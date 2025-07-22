"""Divide3Or5"""
def main():
    """blabla"""
    n = float(input())
    n = int(n)
    summary = 0
    for i in range(1,n+1):
        if not i%3 or not i%5:
            summary += i
        else:
            continue
    print(summary)
main()
