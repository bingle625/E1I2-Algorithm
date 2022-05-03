# 11724번 연결 요소의 개수


import collections
import queue
from sys import stdin


discovered = []
size = 0

dic = collections.defaultdict(list)

N , M  = map(int, input().split())

for _ in range(M):
    u,v = map(int, stdin.readline().split())
    dic[u].append(v)
    dic[v].append(u)
    

def iterative_bfs(start_v):
    discovered.append(start_v)
    queue = collections.deque([start_v])
    while queue:
        v = queue.popleft()
        for w in dic[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return 1

dic_keys = list(dic.keys())

for key in range(1,N+1):
    if key not in discovered:
        size += iterative_bfs(key)
    else:
        continue
print(size)