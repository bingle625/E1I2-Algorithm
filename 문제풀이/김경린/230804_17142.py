from collections import deque
from copy import deepcopy
from re import T
import sys

def is_all_spread(board):
    for i in range(n):
        if 0 in board[i]:
            return False

    return True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split(' '))

board = []
virus = []
for i in range(n):
    tmp = list(map(int, input().split(' ')))
    board.append(tmp)
    for j in range(n):
        if tmp[j] == 2:
            virus.append((j,i))


def spread(old_board, virus):
    board = deepcopy(old_board)
    active_virus = deepcopy(virus)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    while len(active_virus):
        x, y, t = active_virus.popleft()
        # print(active_virus)
        # for b in board:
        #     print(b)
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0<=next_x<n and 0<=next_y<n and visited[next_y][next_x] == 0 and board[next_y][next_x] != 1:
                visited[next_y][next_x] = 1
                board[next_y][next_x] = 2
                active_virus.append((next_x, next_y, t+1))
        
        # print(t,'--------------------------------')
        if is_all_spread(board):
            return t+1
    
    if is_all_spread(board):
        return t+1
    else:
        return -1


min_t = sys.maxsize

cnt = 0
def active(board, idx, active_virus):
    global min_t

    if len(active_virus) == m:
        result = spread(board, active_virus)
        if result != -1:
            min_t = min(min_t, result)
    elif len(active_virus) < m:    
        for i in range(idx, len(virus)):
            active_virus.append((virus[i][0], virus[i][1], 0))
            active(board, i+1, active_virus)
            active_virus.pop()

    
if is_all_spread(board):
    print(0)
else:
    active(board, 0, deque())
    print(min_t if min_t != sys.maxsize else -1)