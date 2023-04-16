

n = int(input())
dp = [0 for _ in range(n+1)]
dp[0] = 1
def fill():
    for i in range(1,n+1):
        if i == 1:
            dp[i] = 1
        elif i>1:
            dp[i] = dp[i-1] + dp[i-2]*2

fill()
print(dp[n]%10007)
