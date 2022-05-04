def maxProfit(stock):
    min = stock[0]
    max = 0
    for i in range(len(stock)-1):
        if stock[i] < stock[i+1]:
            if min > stock[i]:
                min = stock[i]
            if max < stock[i+1]:
                max = stock[i+1]
    if max-min < 0:
        max = 0
        min = 0
    print(max-min)
    return (max-min)


maxProfit([2, 1, 2, 0, 1])
