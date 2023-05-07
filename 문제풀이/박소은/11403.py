# 모든 정점(i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지
# N: vertex#

def DFS(i):
    for j in range(N):
        if visited[j] == 0 and graph[i][j] == 1:
            visited[j] = 1
            DFS(j)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    visited = [0 for _ in range(N)]
    DFS(i)  # i번째 row
    print(*visited)


# 틀린 풀이
"""
from collections import defaultdict

N = int(input())
graph = defaultdict(list)
result = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    array = list(map(int, input().split()))
    for j in range(N):
        if array[j] == 1:
            graph[i].append(j)

def DFS(root):      
    visited = []
    stack = [root]
    print(graph.keys(), 1)

    while stack:
        v = stack.pop()
        if v not in visited:
            print(graph.keys(), 2)
            if v in graph.keys():
                for w in graph[v]:
                    stack.append(w)
                    result[v][w] = 1
                    for visit in visited:
                        result[visit][w] = 1
                        print(graph.keys(), 3)
                visited.append(v)

print(graph.keys())
for key in graph.keys():
    print(key)
    DFS(key)

for i in range(N):
    print(result[i])
"""