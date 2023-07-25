# 국경선 열어야하는지 검사 
# 이차원 배열에 넣어놓기? isOpen[][] = 1
# bfs로 검사해서 

from collections import deque


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, l, r = map(int, input().split(' '))

countries = []

def bfs(visited, i, j):
    tmp = deque()
    saved = []
    tmp.append((j,i))
    saved.append((j,i))
    while len(tmp):
        x, y = tmp.popleft()
        for k in range(4):
            next_x = x+dx[k]
            next_y = y+dy[k]
            if 0<=next_x<n and 0<=next_y<n and visited[next_y][next_x] == 0:
                if l<=abs(countries[y][x] - countries[next_y][next_x])<=r:
                    visited[next_y][next_x] = 1
                    tmp.append((next_x, next_y))
                    saved.append((next_x, next_y))
    return saved, visited


def isBorderOpen():
    global countries

    visited = [[0 for _ in range(n)] for _ in range(n)]
    isChange = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                saved, visited = bfs(visited, i, j)
                if len(saved) > 1:
                    isChange = True
                    value = sum(countries[y][x] for x,y in saved)//len(saved)
                    for x,y in saved:
                        countries[y][x] = value

    return isChange
                
                
                
            





for i in range(n):
    populations =  list(map(int, input().split(' ')))
    countries.append(populations)

day = 0
while isBorderOpen():
    day += 1

print(day)

