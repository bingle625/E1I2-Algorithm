from collections import deque
from sys import stdin

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]


def bfs():
    queue = deque()
    visited = [[0 for _ in range(chess_len)] for _ in range(chess_len)]
    queue.append((start_x,start_y))
    visited[start_y][start_x] = 1
    while len(queue):
        x,y = queue.popleft()
        if x==target_x and y==target_y:
            print(visited[y][x]-1)
            break
        for i in range(8):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x>=0 and next_x<chess_len and next_y>=0 and next_y<chess_len and not visited[next_y][next_x]:
                visited[next_y][next_x] = visited[y][x] + 1
                queue.append((next_x,next_y))
cnt = int(stdin.readline())
for i in range(cnt):
    chess_len = int(stdin.readline())
    start_x, start_y = map(int, stdin.readline().split())
    target_x, target_y = map(int, stdin.readline().split())
    bfs()