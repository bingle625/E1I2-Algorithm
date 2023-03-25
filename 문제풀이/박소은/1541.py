# -가 나온 뒤: 양수를 다 더해서 괄호로 묶는다

line = input()
result = 0
number = 0  # 1~5 자리의 숫자
isMinus = False

for char in line:
    if '0' <= char <= '9':
        number = number*10 + int(char)
    else:
        if char == '+':
            if isMinus == True:
                result -= number
            else:
                result += number
        else:   # '-'인 경우
            if isMinus == False:
                isMinus = True
                result += number
            else:
                result -= number
        number = 0

if isMinus == True:
    result -= number
else:
    result += number

print(result)