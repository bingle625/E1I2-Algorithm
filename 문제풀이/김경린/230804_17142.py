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
blanks = 0
for i in range(n):
    tmp = list(map(int, input().split(' ')))
    board.append(tmp)
    for j in range(n):
        if tmp[j] == 2:
            virus.append((j,i))
        elif tmp[j] == 0:
            blanks += 1


def spread(board, virus, blanks):
    # board = deepcopy(old_board)
    # active_virus = deepcopy(virus)
    active_virus = deque()
    for v in virus:
        active_virus.append(v)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    while (len(active_virus) and blanks > 0):
        x, y, t = active_virus.popleft()
        
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0<=next_x<n and 0<=next_y<n and visited[next_y][next_x] == 0 and board[next_y][next_x] != 1:
                visited[next_y][next_x] = 1
                # board[next_y][next_x] = 2
                active_virus.append((next_x, next_y, t+1))
                if board[next_y][next_x] == 0:
                    blanks -= 1
        
        # print(t,'--------------------------------')
        # if is_all_spread(board):
        #     return t+1
    if blanks == 0:
        return t+1
    else:
        return -1
    
    # if is_all_spread(board):
    #     return t+1
    # else:
    #     return -1


min_t = sys.maxsize

cnt = 0
def active(board, idx, active_virus, blanks):
    global min_t

    if len(active_virus) == m:
        result = spread(board, active_virus, blanks)
        if result != -1:
            min_t = min(min_t, result)
    elif len(active_virus) < m:    
        for i in range(idx, len(virus)):
            active_virus.append((virus[i][0], virus[i][1], 0))
            active(board, i+1, active_virus,blanks)
            active_virus.pop()

    
if blanks == 0:
    print(0)
else:
    active(board, 0, deque(), blanks)
    print(min_t if min_t != sys.maxsize else -1)


# 시간초과 - 직접 board에 접근하는 것이 아닌 빈칸의 개수로 확인하기