
from collections import deque
from sys import stdin




node_num = int(stdin.readline())

tree = [[] for _ in range(node_num+1)]

for i in range(node_num-1):
    node1,node2 = map(int,stdin.readline().split())
    tree[node1].append(node2)
    tree[node2].append(node1)


parent = [0 for _ in range(node_num+1)]
level = [0 for _ in range(node_num+1)]
parent[1] = -1


queue = deque()

def bfs(start):
    queue.append(start)
    while queue:
        start = queue.popleft()
        for i in tree[start]:
            if parent[i]==0:
                parent[i] = start
                level[i] = level[start] + 1
                queue.append(i)


bfs(1)


case = int(input())


for _ in range(case):
    end_1,end_2 = map(int,stdin.readline().split())

    while level[end_1]!=level[end_2]:
        if level[end_1]>level[end_2]:
            end_1 = parent[end_1]
        elif level[end_1]<level[end_2]:
            end_2 = parent[end_2]
    
    while end_1 != end_2:
        end_1 = parent[end_1]
        end_2 = parent[end_2]
    print(end_1)
    
