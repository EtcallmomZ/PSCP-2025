"""progressive tax"""
def main():
    """input"""
    income = int(input())
    tax = 0

    if income > 4000000:
        tax += int((income - 4000000) * 0.35)
        income = 4000000
    if income > 2000000:
        tax += int((income - 2000000) * 0.30)
        income = 2000000
    if income > 1000000:
        tax += int((income - 1000000) * 0.25)
        income = 1000000
    if income > 750000:
        tax += int((income - 750000) * 0.20)
        income = 750000
    if income > 500000:
        tax += int((income - 500000) * 0.15)
        income = 500000
    if income > 300000:
        tax += int((income - 300000) * 0.10)
        income = 300000
    if income > 150000:
        tax += int((income - 150000) * 0.05)
        income = 150000

    print(tax)

main()
