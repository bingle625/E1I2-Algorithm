# 11726번 2xN 타일링
import sys


sys.setrecursionlimit(10**6)

visited = [1, 2]

dp = [0] * 1005

dp[1] = 1
dp[2] = 2


def getFibo(num):
    if num in visited:
        return dp[num]

    visited.append(num)
    dp[num] = getFibo(num-1) + getFibo(num-2)
    return dp[num]


number = int(input())

print(getFibo(number) % 10007)
