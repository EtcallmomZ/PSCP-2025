"""Century"""
def main():
    """input"""
    n = int(input())
    for _ in range(n):
        x = input()
        if  x.startswith("B.E.") or x.startswith("A.D."):
            type_year = x[0:4]
            year = x[5:]
            if type_year == "B.E.":
                convert_year = int(year) - 543
                if not convert_year%100 and convert_year >= 0:
                    print(convert_year // 100)
                elif convert_year % 100 > 0 and convert_year >= 0:
                    print(convert_year // 100 + 1)
                else:
                    print("ERROR")

            else:
                convert_year = int(year)
                if not convert_year%100 and convert_year >= 0:
                    print(convert_year // 100)
                elif convert_year % 100 > 0 and convert_year >= 0:
                    print(convert_year // 100 + 1)
                else:
                    print("ERROR")
        else:
            print("ERROR")

main()
