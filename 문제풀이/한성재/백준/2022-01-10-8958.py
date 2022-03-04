# 8958 OX퀴즈

num = input()

for i in range(int(num)):
    score = 0
    temp_score = 0
    str = input()

    for char in str:

        if(char == 'O'):
            temp_score += 1
        else:
            temp_score = 0

        score += temp_score

    print(score)
