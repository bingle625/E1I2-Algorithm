# 문제 1: 최단경로문제(1) - 18352 실버2

import collections
from sys import stdin, stdout


N, M, K, X = map(int, stdin.readline().rstrip().split())
"""도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X"""

distance = [0]*(N+4)
visited = [False] * (N+1)


def iterative_bfs(start_v):
    result = []
    visited[start_v] = True
    queue = collections.deque([start_v])
    level = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[v] + 1
                if distance[i] == K:
                    result.append(i)
        level += 1

    if len(result) == 0:
        print(-1)
    else:
        result.sort()
        for i in result:
            print(i)


graph = collections.defaultdict(list)
for i in range(M):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)

result_list = iterative_bfs(X)
