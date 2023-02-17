from sys import stdin

n = int(stdin.readline())

dp = [ 0 for _ in range(n+1)]

max_val = 0

for i in range(n):
    day, val = map(int, stdin.readline().rstrip().split(' '))
    max_val = max(max_val, dp[i])
    if day+i > n:
        continue
    dp[i+day] = max(max_val+val, dp[i+day])
    
    


print(max(dp))