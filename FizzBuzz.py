"""FizzBuzz"""
def main():
    """input"""
    x = int(input())
    result = ""

    for i in range(1,x+1):
        if (not i%3) and (not i%5):
            result += "FizzBuzz" + "\n"
        elif not i%3:
            result += "Fizz" + "\n"
        elif not i%5:
            result += "Buzz" + "\n"
        else:
            result += str(i) + "\n"
    print(result,end="")
main()
