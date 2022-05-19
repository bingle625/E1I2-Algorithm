from collections import defaultdict, deque
from sys import stdin

nodeNum = int(stdin.readline().rstrip())
tree = defaultdict(list)

for i in range(nodeNum-1):
    node1, node2 = map(int,stdin.readline().rstrip().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

# node의 높이
pos =defaultdict(int)
pos[1] = 1
parent = [[] for i in range(nodeNum+1)]
parent[1] = [1]
for i in range(1,nodeNum):
    for child in tree[i]:
        if pos[child] == 0:
            pos[child] = pos[i] + 1
            parent[child] = parent[i] + [child]



setNum = int(stdin.readline())
for i in range(setNum):
    node1, node2 = map(int,stdin.readline().split())


    d = min(pos[node1],pos[node2])
    node1 = parent[node1][d-1]
    node2 = parent[node2][d-1]

    while node1 != node2:
        node1 = parent[node1][-1]
        node2 = parent[node2][-1]
    print(parent[node1][d-1])
    
    
