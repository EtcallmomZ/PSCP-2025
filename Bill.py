"""Bill"""
def main():
    """input"""
    a = int(input())
    service = a *0.1
    if service <= 50:
        service = 50

    if service > 1000:
        service = 1000

    vat = (a + service) * 0.07
    amount = a + service + vat
    print(f"{amount:.2f}")

main()
