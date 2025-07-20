"""BrickBridge"""
def main():
    """input"""
    small_brick = int(input())
    large_brick = int(input())
    goal_brick = int(input())
    small_want = 0
    large_have = large_brick * 5
    goal_want = goal_brick // 5
    goal_want = goal_want * 5

    if large_have == goal_brick :
        print(small_want)
    else:
        if large_have < goal_brick:
            small_want = goal_brick - large_have
        else:
            small_want = goal_brick - goal_want

        if small_want <= small_brick:
            print(small_want)
        else:
            small_want = -1
            print(small_want)

main()
