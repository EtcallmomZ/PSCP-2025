"""digital wallet"""
def main():
    """input"""
    name = input()
    nation = input()
    house = input()
    age = float(input())
    salary = float(input())
    fak =  float(input())

    if (nation in ("Yes","True") ) and (house in ("Yes","True")):
        if age >= 16 and fak <= 500000:
            if salary <= 840000:
                print(f"Congratulations! {name} is qualified to receive a digital wallet amount of 10,000 baht,sponsored by all taxpayers in Thailand.")
            else:
                print(f"Unfortunately, {name} is not qualified.")
        else:
            print(f"Unfortunately, {name} is not qualified.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
main()
