"""Turnstile"""
def main():
    """input"""
    total = ""
    while True:
        x = input()
        if x == "END":
            break

        total += x

    print(total.count("CP"))

main()
