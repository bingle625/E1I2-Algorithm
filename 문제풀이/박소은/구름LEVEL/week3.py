# 합 계산기

T = int(input())
sum = 0

for _ in range(T):
    a, char, b = input().split()
    if char == '+':
        sum += int(a) + int(b)
    elif char == '-':
        sum += int(a) - int(b)
    elif char == '*':
        sum += int(a) * int(b)
    elif char == '/':
        sum += int(a) // int(b)

print(sum)