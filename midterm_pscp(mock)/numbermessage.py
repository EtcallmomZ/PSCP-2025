"""number message"""
def main():
    """input"""
    text = input()
    text = text.upper()
    if "13" in text:
        text = text.replace("13","B")
    if "12" in text:
        text = text.replace("12","R")    
    if "1" in text:
        text = text.replace("1","I")
    if "3" in text:
        text = text.replace("3","E")
    if "4" in text:
        text = text.replace("4","A")
    if "5" in text:
        text = text.replace("5","S")
    if "0" in text:
        text = text.replace("0","O")

    new_text = ""


    for i in text:
        if i.isalpha() or i.isspace():
            new_text += i

    print(new_text)




main()
