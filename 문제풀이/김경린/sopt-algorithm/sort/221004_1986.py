
from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().strip().split())

board = [[0 for _ in range(m)] for _ in range(n)]

queen = deque(map(int, stdin.readline().strip(). split()))
queen_num = queen.popleft()
for i in range(len(queen)//2):
    y = queen[2*i]-1
    x = queen[2*i+1]-1
    board[y][x] = 1

knight = deque(map(int, stdin.readline().strip().split()))
knight_num = knight.popleft()
for i in range(len(knight)//2):
    y = knight[2*i]-1
    x = knight[2*i+1]-1
    board[y][x] = 1

pawn = deque(map(int, stdin.readline().strip().split()))
pawn_num = pawn.popleft()
for i in range(len(pawn)//2):
    y = pawn[2*i]-1
    x = pawn[2*i+1]-1
    board[y][x] = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]
diagonal_dx = [1,1,-1,-1]
diagonal_dy = [-1,1,1,-1]

while queen:
    y = queen.popleft()-1
    x = queen.popleft()-1
    for j in range(4):
        new_x = x+diagonal_dx[j]
        new_y = y+diagonal_dy[j]
        while True:
            if 0<=new_x<m and 0<=new_y<n and board[new_y][new_x] != 1:
                board[new_y][new_x] = 2
                new_x += diagonal_dx[j]
                new_y += diagonal_dy[j]
            else:
                break
    for j in range(4):
        new_x = x+dx[j]
        new_y = y+dy[j]
        while True:
            if 0<=new_x<m and 0<=new_y<n and board[new_y][new_x] != 1:
                board[new_y][new_x] = 2
                new_x += dx[j]
                new_y += dy[j]
            else:
                break
            
while knight:
    cur_y = knight.popleft()-1
    cur_x = knight.popleft()-1
    for i in range(4):
        x = (cur_x + dx[i])
        y = (cur_y + dy[i])
        if 0<=x<m and 0<=y<n:
            for j in range(i,i+2):
                new_x = (x+diagonal_dx[j%4])%m 
                new_y = (y+diagonal_dy[j%4])%n
                if 0<=new_x<m and 0<=new_y<n and board[new_y][new_x] != 1:
                    board[new_y][new_x] = 2

cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            cnt += 1
print(cnt)


