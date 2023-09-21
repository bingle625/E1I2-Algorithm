def solution(m, n, puddles):
    answer = 0
    board = [[0 for _ in range(m)] for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(len(puddles)):
        x, y = puddles[i]
        puddles[i] = [x-1, y-1]
    dp[0][0] = 1
    for x in range(m):
        for y in range(n):
            if x == 0 and y == 0:
                continue
            if [x,y] in puddles:
                dp[y][x] = 0
            else:    
                dp[y][x] = (dp[y][x-1] if x >= 1 else 0) + (dp[y-1][x] if y >= 1 else 0)
    return dp[n-1][m-1]%1000000007