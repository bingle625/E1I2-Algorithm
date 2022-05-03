import collections
import heapq
from sys import stdin

num_city = int(stdin.readline())
num_bus = int(stdin.readline())

graph = collections.defaultdict(list)

for i in range(num_bus):
    u,v,w = map(int,stdin.readline().split())
    graph[u].append((v,w))


start,end = map(int,stdin.readline().split())

Q = [(0,start)]

visited = [0 for _ in range(num_bus+1)]
while Q:
    time,node = heapq.heappop(Q)
    if node==end:
        print(time)
        break
    if visited[node]==0:
        visited[node]=1
        for v,w in graph[node]:
            alt = time + w
            heapq.heappush(Q,(alt,v))

