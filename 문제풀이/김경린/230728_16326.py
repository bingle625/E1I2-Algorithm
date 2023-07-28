
from collections import deque


n = int(input())
space = []

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]



for i in range(n):
    tmp = list(map(int, input().split(' ')))
    space.append(tmp)

    for j in range(n):
        if tmp[j] == 9:
            shark_x = j
            shark_y = i
            shark_size = 2


sec = 0
def bfs(shark_x, shark_y, cnt, shark_size):
    global sec, space
    visited = [[0 for _ in range(n)] for _ in range(n)]    
    deq = deque()
    deq.append((shark_x, shark_y, False))
    visited[shark_y][shark_x] = 1
    space[shark_y][shark_x] = 0
    while len(deq):
        x, y, isEatable = deq.popleft()
        if isEatable:
            dist = visited[y][x]
            for temp_x, temp_y, temp_isEatable in deq:
                if temp_isEatable and dist>=visited[temp_y][temp_x]:
                    if y > temp_y:
                        x=temp_x
                        y=temp_y
                    elif y == temp_y and x > temp_x:
                        x=temp_x 
                        y=temp_y
            cnt += 1
            if cnt == shark_size:
                shark_size += 1
                cnt = 0
            sec += visited[y][x]-1
            bfs(x, y, cnt, shark_size)
            break

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0<=next_x<n and 0<=next_y<n and not visited[next_y][next_x]:
                if space[next_y][next_x] <= shark_size:
                    deq.append((next_x, next_y, 0 < space[next_y][next_x] < shark_size))
                    visited[next_y][next_x] = visited[y][x] + 1

bfs(shark_x, shark_y, 0, shark_size)
print(sec)

    