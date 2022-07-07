# 1149 RGB 거리

import sys


inv = int(input())
inArr = []

for i in range(inv):
    inArr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = {}

dp[0] = inArr[0]
for i in range(1, inv):
    dp[i] = []
    for k in range(3):
        minv = sys.maxsize
        for j in range(3):
            if j != k:
                minv = min(minv, dp[i-1][j])
        dp[i].append(inArr[i][k] + minv)

print(min(dp[inv-1]))
