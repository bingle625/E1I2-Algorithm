
        if i-1 in dp:
            mini = min(mini, dp[i-1])
        if i+1 in dp:
            mini = min(mini, dp[i+1])
        if i % 2==0 and i//2 in dp:
            mini = min(mini,dp[i//2])
        dp[i] = mini + 1
