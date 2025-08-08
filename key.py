"""key"""
def main():
    """input"""
    x = input()
    summary = []
    summary.extend(x)

    sum1 = []
    for i in summary:
        n = int(i)
        sum1.append(n)

    plus_13 = sum(sum1)
    long = len(summary)
    last_three_num = sum1[long-3:long]
    last_three_num = str(last_three_num[0]) + str(last_three_num[1]) + str(last_three_num[2])
    last_three_num = int(last_three_num) * 10

    result = plus_13 + last_three_num


    if result > 9999:
        result = str(result)
        long_result = len((result))
        result = result[long_result-4:long_result]
    elif result < 1000:
        result += 1000

    print(result)
main()
