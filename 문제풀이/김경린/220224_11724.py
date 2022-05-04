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
visited_point = deque()



def bfs():
    cnt = 0

    for i in range(1,vertex+1):
        if visited[i-1]==0:
            visited_point.append(i)
            while visited_point:
                point = visited_point.popleft()

                
              
                visited[point-1] = 1
                for j in graph[point]:
                    if visited[j-1]==0:
                        visited[j-1] = 1
                        visited_point.append(j)
                        
    

            cnt += 1
                    
    return cnt


    
        


print(bfs())