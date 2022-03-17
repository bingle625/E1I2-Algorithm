
from collections import defaultdict, deque
from sys import stdin

graph = defaultdict(deque)


node_num = int(stdin.readline())


visited = [0 for _ in range(node_num+1)]

for i in range(node_num-1):
    node_1,node_2 = map(int,stdin.readline().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)


deq = deque()
deq.append(1)
visited[1] = 1

def bfs(deq):
    cnt = 0
    while len(deq):
        node = deq.popleft()
        for child in graph[node]:
            if visited[child]==0:
                visited[child]=1
                deq.append(child)

                if len(graph[child])>1 or node==1:
                    cnt+=1




    print(cnt)

bfs(deq)

                

    