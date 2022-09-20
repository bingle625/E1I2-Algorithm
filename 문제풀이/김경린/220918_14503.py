from collections import deque
from sys import stdin
n, m = map(int, stdin.readline().split())
area = [ [0 for _ in range(m+2)] for _ in range(n+2)]

startY, startX, dir = map(int,stdin.readline().split())
startY += 1
startX += 1

for i in range(n+2):
    if i == 0 or i == n+1:
        area[i] = [1 for _ in range(m+2)]
    else:
        tmp = deque(map(int, stdin.readline().split()))
        tmp.appendleft(1)
        tmp.append(1)
        area[i] = tmp

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x = startX
y = startY

def cleaner(x, y, d, cnt):
    if not area[y][x]:
        cnt += 1
    for i in range(1,5):
        dir = d - i if d-i >= 0 else d-i+4
        area[y][x] = 2
        nextX = x + dx[dir]
        nextY = y + dy[dir]
        if not area[nextY][nextX]:
            x = nextX
            y = nextY
            cleaner(x, y, dir, cnt)
    nextX = x + dx[(dir+2)%4]
    nextY = y + dy[(dir+2)%4]
    if area[nextY][nextX] != 1:
        cleaner(nextX,nextY,dir,cnt)
    else:
        print(cnt)
        exit()

cleaner(x, y, dir, 0)
    
    
        
