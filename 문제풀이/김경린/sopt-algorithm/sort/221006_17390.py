from sys import stdin


length, question = map(int,stdin.readline().strip().split())
nums = list(map(int, stdin.readline().strip().split()))
nums.sort()

dp = [ 0 for _ in range(length+1)]

for i in range(1, length+1):
    dp[i] = dp[i-1] + nums[i-1]

for i in range(question):
    start, end = map(int,stdin.readline().strip().split())
    sum = dp[end] - dp[start-1]
    print(sum)                                                  



