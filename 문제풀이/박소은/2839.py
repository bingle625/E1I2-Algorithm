# N: 배달해야 하는 설탕 무게
# 3kg 봉지, 5kg 봉지
import math

N = int(input())
if (N < 3):
    print(-1)

dp = [math.inf for _ in range(N + 1)]
# dp[8]: 8kg을 들 때 가져가야 하는 봉지 개수
dp[3] = 1
dp[5] = 1

for i in range(6, N+1):
    dp[i] = dp[i-3]+1 if dp[i-3]<dp[i-5] else dp[i-5]+1

if dp[N] == math.inf: 
    print(-1)
else:
    print(dp[N])