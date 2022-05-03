# 85번 피보나치
import collections


class Solution(object):  
    # # 풀이1. 재귀 구조 브루트 포스
    # def fib(self, N: int)->int:
    #     if N <= 1:
    #         return N
    #     return self.fib(N-1) + self.fib(N-2)
    
    # # 풀이 2. 하향식 메모이제이션
    # dp = collections.defaultdict(int)
    # def fib(self, N: int) -> int:
    #     if N <= 1:
    #         return N
        
    #     if self.dp[N]:
    #         return self.dp[N]
    #     self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
    #     return self.dp[N]
    
    # # 풀이 3. 타뷸레이션
    # dp = collections.defaultdict(int)
    
    # def fib(self, N: int) -> int:
    #     self.dp[0] = 0
    #     self.dp[1] = 1
        
    #     for i in range(2, N+1):
    #         self.dp[i] = self.dp[i-1] + self.dp[i-2]
        
    #     return self.dp[N]
    
    # # 풀이 4. 두 변수만 이용해 공간 절약
    
    # def fib(self, N: int) -> int:
    #     x,y = 0,1
    #     for i in range(0,N):
    #         x,y = y, x+y
    #     return x
    
    # 풀이 5. 행렬