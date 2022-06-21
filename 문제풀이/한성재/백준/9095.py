# 9095번 1,2,3더하기

# dp
from sys import stdin


dp = [0]*15
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
visited = [1, 2, 3, 4]

number = int(input())


def getSumComb(N):
    if N in visited:
        return dp[N]

    sum1 = 0
    sum1 += getSumComb(N-1)
    sum1 += getSumComb(N-2)
    sum1 += getSumComb(N-3)

    dp.append(N)
    return(sum1)


for i in range(number):
    num = stdin.readline().rstrip()
    num = int(num)

    print(getSumComb(num))
