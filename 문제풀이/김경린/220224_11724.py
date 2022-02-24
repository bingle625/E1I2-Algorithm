from collections import defaultdict
from collections import deque
from sys import stdin

graph = defaultdict(deque)
vertex,edge = map(int,stdin.readline().split())

for i in range(edge):
    point1,point2 = map(int,stdin.readline().split())
    graph[point1].append(point2)
    graph[point2].append(point1)

visited = [0 for _ in range(vertex)]

cnt = 0


def dfs(i):
    if len(graph[i])>0:
        while graph[i]:
            point = graph[i].popleft()
            if visited[point-1]==0:
                visited[point-1] = 1
                dfs(point)
                
        done = 1
    else:
        done = 0
    return done
    
        

visited[0]=1
for i in range(1,vertex+1):
   
    done = dfs(i)
    if done==1:
        cnt+=1
print(cnt)