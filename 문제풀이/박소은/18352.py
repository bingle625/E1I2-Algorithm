# N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시의 번호
import collections
import heapq
import sys

inputNums = str(sys.stdin.readline())
N, M, K, X = map(int, inputNums.split())
edge = []
for _ in range(M):
    edge.append(list(map(int, str(sys.stdin.readline()).split())))
graph = collections.defaultdict(list)

# 그래프 인접 리스트 구성
for u, v in edge:
    graph[u].append(v)

# 큐 변수: [(소요 시간, 정점)]
Q = [(0, X)]
dist = collections.defaultdict(int)
dist[X] = 0     # 시작 노드는 소요 시간=0

# 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입(BFS)
while Q:
    time, node = heapq.heappop(Q)
    for adjNode in graph[node]:
        if adjNode not in dist or dist[adjNode] > time+1:
            dist[adjNode] = time+1
            heapq.heappush(Q, (time+1, adjNode))

result = []
print(dist)
for key, val in dist.items():
    if val == K:
        result.append(key)

if not result:
    print(-1)
else:
    result.sort()
    for elem in result:
        print(elem)