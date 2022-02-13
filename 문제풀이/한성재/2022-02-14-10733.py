# 10733번
# 제로

from sys import stdin

num = int(stdin.readline())

stack = []
sum = 0

for _ in range(num):
    num2 = int(stdin.readline())
    if num2 == 0:
        sum = sum - stack.pop()
    else:
        stack.append(num2)
        sum += stack[-1]

print(sum)
