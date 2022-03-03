
from collections import deque
from sys import stdin

node_num = int(stdin.readline())

tree = [[] for _ in range(node_num+1)]

for i in range(node_num-1):
    node1,node2 = map(int,stdin.readline().split())
    tree[node1].append(node2)
    tree[node2].append(node1)



global end

queue = deque()

def bfs(start):
    global end
    queue.append(start)
    while queue:
        start = queue.popleft()
        for i in tree[start]:
            if visited[i]==0:
                visited[i] = str(i)
                queue.append(i)
                visited[i] = visited[start]+'-'+str(i)
                if i == end:
                    queue.clear()
                    return visited[i]



case = int(input())


for i in range(case):
    end_1,end_2 = map(int,stdin.readline().split())

    visited = [0 for _ in range(node_num+1)]
    visited[1]="1"

    end = end_1
    path_1=bfs(1)

    
    
    visited = [0 for _ in range(node_num+1)]
    visited[1]="1"
    end = end_2
    
    path_2 = bfs(1)

    path_1 = deque(path_1.split('-'))
    path_2 = deque(path_2.split('-'))
    
    for i in range(len(path_1)):
        top_1 = path_1.popleft()
        top_2 = path_2.popleft()
        if len(path_1) and len(path_2):
            if path_1[0]!=path_2[0]:
                print(top_1)
                break
        else:
            print(top_1)

    