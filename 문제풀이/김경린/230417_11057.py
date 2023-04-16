

n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(10):
        if i == 1:
            dp[i][j] = 1
        else:
            for k in range(j+1):
                dp[i][j] += dp[i-1][k]
print(sum(dp[n])%10007)