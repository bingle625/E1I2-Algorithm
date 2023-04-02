import sys
sys.setrecursionlimit(10**6)    # recursion 깊이가 너무 작아서 런타임 에러 발생

# BFS로 탐색하는 경우: **중복 방문을 막으려면 큐에 넣을 때 체크**


def findWormNum(n: int, m: int, cabNum: int) -> int:
    grid = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(cabNum):
        i, j = map(int, input().split())
        grid[i][j] = 1
        
    def dfs(i, j):
        if i<0 or i>=n or j<0 or j>=m or grid[i][j] != 1:   # 배추가 아니면 탐색 종료
            return
        grid[i][j] = 0  # 방문한 배추는 0으로 표시
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    worms = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dfs(i, j)
                worms += 1
            
    return worms

T = int(input())
answer = []
for _ in range(T):
    n, m, cabNum = map(int, input().split())
    answer.append(findWormNum(n, m, cabNum))

for elem in answer:
    print(elem)