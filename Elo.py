"""Elo"""
import math
def main():
    """input"""
    ra = int(input())
    rb = int(input())
    choice = input()
    if choice  == "A":
        print(f"{1/(1+ math.pow(10,(rb-ra)/400)):.2f}")
    else:
        print(f"{1/(1+ math.pow(10,(ra-rb)/400)):.2f}")

main()
