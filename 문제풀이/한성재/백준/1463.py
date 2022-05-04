import sys
#1463번 1로 만들기


dp = dict()
dp[0] = 0
dp[2] = 1
dp[3] = 1

def goN(n:int):
    if n == 1:
        return 0
    
    for i in range(n+1):
        mini = sys.maxsize
        if i in dp:
            continue
        else:
            if i%2 == 0:
                mini = min(dp[i // 2],mini)
            if i%3 == 0:
                mini = min(dp[i//3], mini)
            mini = min(dp[i-1],mini)
            dp[i] = mini + 1
    
    return dp[n]

number = int(input())

print(goN(number))
