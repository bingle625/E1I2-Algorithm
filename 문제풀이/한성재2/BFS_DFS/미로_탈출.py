# 미로 탈출 0325 ~ 0355
from collections import deque


N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))


def bfs(graph, start):
    cnt = 0
    ready_q = deque([start])
    cur_q = deque([])
    while True:
        cnt += 1
        while ready_q:
            cur_q.append(ready_q.popleft())
        while cur_q:
            cur = cur_q.popleft()
            if cur == (N-1, M-1):
                return cnt

            graph[cur[0]][cur[1]] = 0

            if cur[0] - 1 >= 0 and graph[cur[0]-1][cur[1]] == 1:
                ready_q.append((cur[0]-1, cur[1]))
            if cur[0] + 1 < N and graph[cur[0]+1][cur[1]] == 1:
                ready_q.append((cur[0]+1, cur[1]))
            if cur[1] - 1 >= 0 and graph[cur[0]][cur[1]-1] == 1:
                ready_q.append((cur[0], cur[1]-1))
            if cur[1] + 1 < M and graph[cur[0]][cur[1]+1] == 1:
                ready_q.append((cur[0], cur[1]+1))


print(bfs(graph, (0, 0)))


# bfs는 간선의 길이가 모두 같을 때, 최단거리를 찾기위해서 수행할 수 있음.
