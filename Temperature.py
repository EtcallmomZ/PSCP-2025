"""Temperature"""
x = float(input())
tem1 = input()
tem2 = input()

def c():
    '''celceius'''
    if tem2 == "K":
        k_tem = x + 273.15
        print(f"{k_tem:.2f}")
    elif tem2 == "F":
        result = x * 9 / 5 + 32
        print(f"{result:.2f}")
    elif tem2 == "R":
        result = (x + 273.15) * 9 / 5
        print(f"{result:.2f}")
    else:
        print(x)

def k():
    '''kelvin'''
    if tem2 == "C":
        c_tem = x - 273.15
        print(f"{c_tem:.2f}")
    elif tem2 == "F":
        result = (x - 273.15) * 9 / 5 + 32
        print(f"{result:.2f}")
    elif tem2 == "R":
        result = x * 9 / 5
        print(f"{result:.2f}")
    else:
        print(x)

def f():
    '''falen'''
    if tem2 == "C":
        c_tem = ( x - 32 )* 5 / 9
        print(f"{c_tem:.2f}")
    elif tem2 == "K":
        k_tem = ((x - 32 )* 5 / 9) + 273.15
        print(f"{k_tem:.2f}")
    elif tem2 == "R":
        result = ((( x - 32 )* 5 / 9) + 273.15) * 9/5
        print(f"{result:.2f}")
    else:
        print(x)

def r():
    '''rankine'''
    if tem2 == "C":
        c_tem = x * 5 / 9 - 273.15
        print(f"{c_tem:.2f}")
    elif tem2 == "K":
        result = (x * 5 / 9 - 273.15) + 273.15
        print(f"{result:.2f}")
    elif tem2 == "F":
        result = (x * 5 / 9 - 273.15) * 9 / 5 + 32
        print(f"{result:.2f}")
    else:
        print(x)

if tem1 == "C":
    c()
elif tem1 == "K":
    k()
elif tem1 == "F":
    f()
else:
    r()
