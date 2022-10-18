# 음료수 얼려먹기 30분 0211 ~ 0241

from collections import deque


N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for i in range(N)]


visited = [[False]*M for i in range(N)]


cnt = 0


def bfs(graph, start, visited):
    q = deque([start])
    while q:
        cur = q.popleft()
        x = cur[0]
        y = cur[1]
        if x+1 < N and graph[x+1][y] == 0:
            if visited[x+1][y] == False:
                q.append((x+1, y))
                visited[x+1][y] = True
        if y+1 < M and graph[x][y+1] == 0:
            if visited[x][y+1] == False:
                q.append((x, y+1))
                visited[x][y+1] = True
        if x-1 > 0 and graph[x-1][y] == 0:
            if visited[x-1][y] == False:
                q.append((x-1, y))
                visited[x-1][y] = True
        if y-1 > 0 and graph[x][y-1] == 0:
            if visited[x][y-1] == False:
                q.append((x, y-1))
                visited[x][y-1] = True


for i in range(N):
    for k in range(M):
        if graph[i][k] == 0:
            if visited[i][k] == False:
                bfs(graph, (i, k), visited)
                cnt += 1

print(cnt)
