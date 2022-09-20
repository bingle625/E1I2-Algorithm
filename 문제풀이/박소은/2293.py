# 2293번 동전1 문제: DP
# 동전 종류: n가지
# 가치의 합: k원

# ex) 3 10
# 1
# 2
# 5
from collections import defaultdict

n, k = map(int, input().split())
valList = [int(input() for _ in range(n))]  # 코인의 종류

dp = [0 for _ in range(k + 1)]  # 사이즈 k+1 만큼의 리스트 선언
# dp[1]: 합이 1원이 되는 경우의 수, dp[2]: 합이 2원이 되는 경우의 수 ...
dp[0] = 1   # 0원이 되는 경우의 수는 1가지

for val in valList: # [1,2,5] 순회하면서 동전 사용하기
    for i in range(val, k + 1):
        # 1원짜리 동전을 사용했을 때 만들 수 있는 경우를 dp에 저장
        if i - val >= 0:
            dp[i] += dp[i - 1]

print(dp[k])