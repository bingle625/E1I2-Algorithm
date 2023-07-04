from copy import deepcopy
from sys import stdin


n, m = map(int, stdin.readline().split(' '))

maps = []
for i in range(n):
    row = list(map(int,stdin.readline().split(' ')))
    maps.append(row)

wall_num = 3
max_safe = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def get_safe(maps):
    cnt = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 0:
                cnt += 1
    return cnt

def spread_virus(maps, x, y, visited):
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < m and 0 <= next_y < n and maps[next_y][next_x] == 0:
            visited[next_y][next_x] = 1
            maps[next_y][next_x] = 2
            spread_virus(maps, next_x, next_y, visited)

def create_wall(x, y, m, n, maps, wall_num):
    global max_safe
    if wall_num == 0:
        visited = [ [0 for _ in range(m)] for _ in range(n)]
        for y in range(n):
            for x in range(m):
                if maps[y][x] == 2 and visited[y][x] == 0:
                    visited[y][x] = 1
                    spread_virus(maps, x, y, visited)
        
        safe = get_safe(maps)
        max_safe = max(max_safe, safe)
    else:
        for i in range(n):
            for j in range(m):
                if i*m + j > y*m + x and maps[i][j] == 0:
                    maps[i][j] = 1
                    create_wall(j, i, m, n, deepcopy(maps), wall_num-1)
                    maps[i][j] = 0
                    
for y in range(n):
    for x in range(m):
        if maps[y][x] == 0:
            maps[y][x] = 1
            create_wall(x,y,m,n,maps, wall_num-1)            
            maps[y][x] = 0

print(max_safe)