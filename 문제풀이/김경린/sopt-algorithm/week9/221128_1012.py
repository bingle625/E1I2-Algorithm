
from collections import deque
from sys import stdin

case = int(stdin.readline())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(temp):
    while len(temp):
        x, y = temp.popleft()
        for j in range(4):
            next_y = y +dy[j]
            next_x = x + dx[j]
            if next_y>=0 and next_y<n and next_x>=0 and next_x<m and farm[next_y][next_x] == 1 and not visited[next_y][next_x]:
                temp.append((next_x,next_y))
                visited[next_y][next_x] = 1

    
for i in range(case):
    m, n, cabbage = map(int, stdin.readline().split())
    farm = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(cabbage):
        x, y = map(int, stdin.readline().split())
        farm[y][x] = 1
    temp = deque()
    cnt = 0
    for y in range(n):
        for x in range(m):
            if farm[y][x] == 1 and not visited[y][x]:
                temp.append((x,y))
                visited[y][x] = 1
                bfs(temp)
                cnt += 1
    print(cnt)
