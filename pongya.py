"""pongya"""
def main():
    """input"""
    x = int(input())
    if not x % 3 or str(x).endswith("3"):
        print("PONG")
    else:
        print(x)
main()
