
test_num = int(input())

for i in range(test_num):
    line = input()
    line_list = list(line)
    score = 0
    score_sum = 0

    for j in line_list:
        if j == 'O':
            score += 1
            score_sum += score
        else:
            score = 0

    print(score_sum)

