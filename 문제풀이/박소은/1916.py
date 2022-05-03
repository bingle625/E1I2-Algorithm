import collections
import heapq

def minCost(graph, startNum: int, endNum: int):
    # 큐 변수: [(소요 시간, 정점)]
    Q = [(0, startNum)]
    dist = collections.defaultdict(int)

    while Q:
        price, node = heapq.heappop(Q)
        if node == endNum:
            return price

        if node not in dist:
            dist[node] = price
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v))

graph = collections.defaultdict(list)
# 입력
N = int(input())
M = int(input())
for info in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
startNum, endNum = map(int, input().split())
print(minCost(graph, startNum, endNum))