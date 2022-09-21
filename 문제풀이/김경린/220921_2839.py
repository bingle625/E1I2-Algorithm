from sys import stdin
w = int(stdin.readline())
dp = [5000 for _ in range(w+1)]

# def dp(w):
#     print(w)
#     if w == 0:
#         return 0
#     elif w < 3:
#         return 5000
#     elif data[w] != 0:
#         return data[w]
#     else:
dp[0] = 0
for i in range(3,w+1):
    if i>=5:
        dp[i] = min(dp[i-3], dp[i-5])+1
    else:
        dp[i] = dp[i-3] + 1
if dp[w]>=5000:
    print(-1)
else:
    print(dp[w])