"""GCD_N"""
import math
def main():
    """input"""
    n = int(input())
    t_1 = []
    for _ in range(n):
        x = int(input())
        t_1.append(x)

    gcd_result = t_1[0]
    for i in t_1[1:]:
        gcd_result = math.gcd(gcd_result,i)

    print(gcd_result)
main()
