# 구역 문제 -> DFS
import sys
sys.setrecursionlimit(10**6)

def DFS(i, j, color):
    if i<0 or i>=N or j<0 or j>=N or graph[i][j] != color:  # 구역을 벗어났을 경우
        return
    
    if graph[i][j] == 'B':
        graph[i][j] = 1
    elif graph[i][j] == 'R' or graph[i][j] == 'G':
        graph[i][j] = 2
    else:   # 적록색약이 탐색할 때 
        graph[i][j] = 0
    
    DFS(i+1, j, color)
    DFS(i-1, j, color)
    DFS(i, j+1, color)
    DFS(i, j-1, color)



N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))

colorWeakness = 0   # 적록색약이 있는 사람이 본 구역의 수
allColor = 0    # 적록색약 없는 사람이 본 구역의 수

# 적록색약 없는 사람
for i in range(N):
    for j in range(N):
        if graph[i][j] != 1 and graph[i][j] != 2:
            DFS(i, j, graph[i][j])
            allColor += 1

# 적록색약 있는 사람
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            DFS(i, j, graph[i][j])
            colorWeakness += 1

print(allColor, colorWeakness)