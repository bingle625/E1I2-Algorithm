# 14501 퇴사

from sys import stdin


num = int(input())
period = []
price = []
dp = [0] * num

for i in range(num):
    a, b = map(int, input().split())
    period.append(a)
    price.append(b)

for i in range(num-1, -1, -1):
    dp[i] =
