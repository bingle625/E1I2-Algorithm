def cal_score(test):
    score = 0
    sum = 0
    for string in test:
        if string == 'O':
            score += 1
        elif string == 'X':
            score = 0
        sum += score
    return sum


case = int(input())

for i in range(case):
    test = str(input())
    print(cal_score(test))
