# 그래프 탐색 문제 -> DFS

from typing import List
import sys
sys.setrecursionlimit(10**6)

def numOfSafetyArea(height):
    # height 이하인 지점은 물에 잠긴다. height를 초과하면 안전 영역
    visited = [[1 for _ in range(n)] for _ in range(n)]
    
    def DFS(i: int, j: int, visited: List):
        # 더 이상 안전 영역이 아닌 경우 종료
        if i<0 or i>=n or j<0 or j>=n or grid[i][j]<=height or visited[i][j] == 0:
            return
        
        visited[i][j] = 0   # 탐색한 안전 영역은 0(위험 영역)으로 표시

        # 동서남북 탐색
        DFS(i+1, j, visited)
        DFS(i-1, j, visited)
        DFS(i, j+1, visited)
        DFS(i, j-1, visited)
    
    count = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] > height and visited[i][j] == 1:
                DFS(i, j, visited)
                count += 1
    return count


# 입력
n = int(input())
grid = []
maxHeight = 0
minHeight = 101
maxSafetyArea = 1

for i in range(n):
    grid.append(list(map(int, input().split())))
    maxHeight = max(max(grid[i]), maxHeight)
    minHeight = min(min(grid[i]), minHeight)

for i in range(minHeight, maxHeight):
    maxSafetyArea = max(maxSafetyArea, numOfSafetyArea(i))
    
print(maxSafetyArea)