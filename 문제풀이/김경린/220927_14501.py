from collections import deque
from sys import stdin

deadline = int(stdin.readline())

dp = [ 0 for _ in range(deadline+1)]

for i in range(1,deadline+1):
    day, pay = map(int, stdin.readline().split())
    dp[i] = max(dp[i-1], dp[i])
    if day + i-1 <= deadline:
        dp[day+i-1] = max(dp[day+i-1],dp[i-1]+pay)

print(max(dp))
