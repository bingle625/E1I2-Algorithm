from collections import deque


N,M = map(int,input().split())

graph = []
pos = []
virus = []

temp = list([0]*M for i in range(N))

visited = list([False]*M for i in range(N))
for i in range(N):
    graph.append(list(map(int, input().split())))


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            pos.append((i,j))
        elif graph[i][j] == 2:
            virus.append((i,j))
maxi = 0

# 상 하 좌 우
dxy = [(-1,0),(1,0),(0,-1),(0,1)]

def _bfs(graph,pos):
    
    q = deque([pos])
    
    while q:
        cur = q.popleft()
        temp[cur[0]][cur[1]] = 3
        
        for i in range(4):
            nx = cur[0] + dxy[i][0]
            ny = cur[1] + dxy[i][1]
            if nx < 0 or nx >=N:
                continue
            if ny < 0 or ny >=M:
                continue
            if temp[nx][ny] == 0 or temp[nx][ny] == 2:
                q.append((nx,ny))
    return True    

def bfs():
    for i in range(N):
        for k in range(M):
            temp[i][k] = graph[i][k]
    
    for virus_pos in virus:
        _bfs(graph,virus_pos)
        
    cnt = 0
    for i in range(len(pos)):
        if temp[pos[i][0]][pos[i][1]] == 0:
            cnt += 1
    return cnt


for i in range(len(pos)):
    x,y = pos[i][0], pos[i][1]
    for j in range(i+1,len(pos)):
        for k in range(j+1,len(pos)):
            graph[x][y],graph[pos[j][0]][pos[j][1]],graph[pos[k][0]][pos[k][1]] = 1,1,1
            maxi = max(maxi,bfs())
            graph[x][y],graph[pos[j][0]][pos[j][1]],graph[pos[k][0]][pos[k][1]] = 0,0,0

print(maxi)