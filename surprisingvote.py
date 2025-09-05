"""Surprising Vote"""
def main():
    """input"""
    summary = float(input())
    max_score = float(input())

    two_person_score = summary - max_score
    min_score = max(0,two_person_score - 10)




    if (max_score-min_score) > 2:
        print("Surprising")
    else: 
        print("Not surprising")

main()
