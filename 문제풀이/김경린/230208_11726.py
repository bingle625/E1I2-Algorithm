# 9
# 2 2 2 2 1   5
# 2 2 2 1 1 1   20
# 2 2 1 1 1 1 1   21
# 2 1 1 1 1 1 1 1   8
# 1 1 1 1 1 1 1 1 1  1


# dp[n] = dp[n-1] + dp[n-2]

# n = int(input())

# dp = [0 for _ in range(n+1)]

# def rectangle(n):
#     if n <= 1:
#         return 1
#     if dp[n] != 0:
#         return dp[n]
#     dp[n] = rectangle(n-1) + rectangle(n-2)
#     return dp[n]

# dp[0] = 1
# dp[1] = 1

# print(rectangle(n)%10007)

words = ["cat", "listen", "silent", "kitten", "salient"]

for i in range(len(words)):
    words[i] = words[i].sorted()
print(words)
print(len(set(words)))