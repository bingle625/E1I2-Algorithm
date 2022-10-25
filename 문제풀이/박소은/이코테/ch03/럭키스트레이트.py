N = int(input())
digit = 2

# 자릿수 구하기
while True:
    if N % pow(10, digit) == N:
        break
    else:
        digit += 1

num1 = N // pow(10, digit//2)   # 왼쪽 부분
num2 = N % pow(10, digit//2)    # 오른쪽 부분

num1Sum, num2Sum = 0, 0
for i in range(1, digit//2 + 1):
    num1Sum += num1 % 10
    num1 = num1 // 10
    num2Sum += num2 % 10
    num2 = num2 // 10

if num1Sum == num2Sum:
    print('LUCKY')
else:
    print('READY')
