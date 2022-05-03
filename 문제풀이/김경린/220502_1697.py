from collections import deque


ob,yb = map(int,input().split())

visited = [ 0 for _ in range(1000000)]
graph = deque()
graph.append(ob)
visited[ob] = 0
def bfs():
    while True:
        x = graph.popleft()
        if x == yb :
            return visited[x]
    
        if 2*x>=0 and 2*x<=100000 and visited[2*x]==0 and x != 0: 
            visited[2*x] = visited[x] + 1
            graph.append(2*x)
        if x+1>=0 and x+1<=100000 and visited[x+1]==0: 
            visited[x+1] = visited[x] + 1
            graph.append(x+1)
        if x-1>=0 and x-1<=100000 and visited[x-1]==0:
            visited[x-1] = visited[x] + 1  
            graph.append(x-1)


print(bfs())