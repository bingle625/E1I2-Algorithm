
from collections import deque
from sys import stdin

node_num = int(stdin.readline())

tree = [[] for _ in range(node_num+1)]

for i in range(node_num-1):
    node1,node2 = map(int,stdin.readline().split())
    tree[node1].append(node2)
    tree[node2].append(node1)



global end


def dfs(start):
    global end
    for child in tree[start]:
        if visited[child]==0:
            if child==end :
                path.append(child)
                return 1
            visited[child] = 1
            discover = dfs(child)
            if discover==1:
                path.append(child)
                return 1


case = int(input())


for i in range(case):
    end_1,end_2 = map(int,stdin.readline().split())

    visited = [0 for _ in range(node_num+1)]
    visited[1]=1
    path = []
    end = end_1
    dfs(1)
    path.append(1)
    path_1 = path[:]
    
    visited = [0 for _ in range(node_num+1)]
    visited[1]=1
    end = end_2
    path = []
    dfs(1)
    path_2 = path[:]

    
    path_2.append(1)
    
    for i in range(len(path_1)):
        top_1 = path_1.pop()
        top_2 = path_2.pop()
        if len(path_1) and len(path_2):
            if path_1[-1]!=path_2[-1]:
                print(top_1)
                break
        else:
            print(top_1)

    