from collections import deque
from sys import stdin


dx = [1,0,-1,0]
dy = [0,1,0,-1]


def countArea(i,j):
    col = len(picture[0])
    row = len(picture)
    x = i
    y = j
    path = deque()
    path.append((x,y))
    visited[y][x] = 1
    while len(path):
        x,y = path.popleft()
        for i in range(4):
            if 0 <= x+dx[i] <col and 0 <= y+dy[i] < row: 
                    if picture[y][x] == picture[y+dy[i]][x+dx[i]] and not visited[y+dy[i]][x+dx[i]]:
                        visited[y+dy[i]][x+dx[i]] = 1
                        path.append((x+dx[i], y+dy[i]))



n = int(stdin.readline())
picture = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
color = 0
non_color = 0
for i in range(n):
    str = stdin.readline()
    picture[i] = list(str)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            countArea(j,i)
            color += 1

for i in range(n):
    for j in range(n):
        if picture[i][j]=='R':
            picture[i][j] = 'G'
        visited[i][j] = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            countArea(j,i)
            non_color += 1




print("%d %d" %(color, non_color))
