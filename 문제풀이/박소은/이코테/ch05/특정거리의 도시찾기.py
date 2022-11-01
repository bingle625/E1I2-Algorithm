# p.339 특정 거리의 도시 찾기
# 1~N번까지의 도시, M개의 단방향 도로. 모든 도로의 거리는 1
# X도시로부터 출발하여 도달할 수 있는 도시 중 최단거리가 K인 도시를 출력

from collections import defaultdict, deque

graph = defaultdict(list)
result = defaultdict(int)

N, M, K, X = map(int, input().split())
for _ in range(M):
    # a 도시 -> b 도시 단방향 도로
    a, b = map(int, input().split()) 
    graph[a].append(b)

queue = deque([X])
distance = 0
while queue:
    v = queue.popleft()
    distance += 1   # 한 번 탐색할 때마다 거리+1
    for i in graph[v]:
        if result[i] == 0:  # 방문하지 않은 곳일 때
            queue.append(i)
            result[i] += distance

answer = [key for key, value in result.items() if value == K]
if answer:
    print(*answer, sep='\n')
else:
    print(-1)