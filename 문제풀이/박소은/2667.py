# 그래프 탐색 -> DFS
import sys
sys.setrecursionlimit(10**6)

def DFS(i, j, houseNum):
    if i<0 or i>=N or j<0 or j>=N or graph[i][j] == '0':
        return
    
    graph[i][j] = '0'
    houses[houseNum] += 1
    
    DFS(i+1, j, houseNum)
    DFS(i-1, j, houseNum)
    DFS(i, j+1, houseNum)
    DFS(i, j-1, houseNum)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))
    
houseNum = 0
houses = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            houses.append(0)
            DFS(i, j, houseNum)
            houseNum += 1

print(houseNum)
houses.sort()
for house in houses:
    print(house)