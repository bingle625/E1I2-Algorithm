
from collections import deque
import sys

def bfs(j,i):
    for k in range(4):
        next_dy = i+dy[k]
        next_dx = j+dx[k]
        if next_dx>=0 and next_dx<M and next_dy>=0 and next_dy<N and tomato[next_dy][next_dx]==0:
            visited.append([next_dx,next_dy])
            tomato[next_dy][next_dx] = tomato[i][j]+1


dx = [0,1,0,-1]
dy = [-1,0,1,0]

M,N = map(int,input().split())

tomato = [[0]*M for _ in range(N)]
visited = deque()

for i in range(N):
    tomato[i] = list(map(int,input().split()))




# 처음 시작 토마토를 찾기 위해 전체 탐색
for i in range(N):
    for j in range(M):
        if tomato[i][j]==1:
            visited.append([j,i])



if visited:
    while visited:
        tomato_pos = visited.popleft()
        x,y = tomato_pos[0],tomato_pos[1]
        bfs(x,y)

    #익지 않은 토마토가 있을 경우
    for i in range(N):
        for j in range(M):
            if tomato[i][j]==0:
                print(-1)
                sys.exit(0)

#시작을 1일로 잡아서 -1
    print(tomato[y][x]-1)

else:
    print(-1)