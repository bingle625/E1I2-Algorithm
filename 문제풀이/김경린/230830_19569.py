import sys

val = int(input())
items = list(map(int, input().split(' ')))

dp = [ sys.maxsize for _ in range(val+1)]
dp[0] = 0

def recovery(n):
    for i in range(1, n+1):
        if i-items[0] >= 0 and dp[i-items[0]] != sys.maxsize:
            dp[i] = min(dp[i-items[0]] + 1, dp[i])
        if i-items[1] >= 0 and dp[i-items[1]] != sys.maxsize: 
            dp[i] = min(dp[i-items[1]] + 1, dp[i])
    
recovery(val)
print(dp[val] if dp[val] != sys.maxsize else -1)