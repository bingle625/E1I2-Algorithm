
inputStr = input()
result = []
sum = 0

for char in inputStr:
    if char.isdigit():
        # 숫자인 경우
        sum += int(char)
    else:
        result.append(char)

# sorted(result)
result.sort()
print(''.join(result) + str(sum))