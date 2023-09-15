# 백트래킹
from sys import stdin
board = []
zeros = []

for y in range(9):
    tmp = list(map(int, stdin.readline().rstrip().split(' ')))
    board.append(tmp)
    for x in range(9):
        if tmp[x] == 0:
            zeros.append((x, y))

def is_duplicated_x(y, val):
    for i in range(9):
        if board[y][i] == val:
            return True
    return False

def is_duplicated_y(x, val):
    for i in range(9):
        if board[i][x] == val:
            return True
    return False

def is_duplicated_square(x, y, val):
    start_x = x//3*3
    start_y = y//3*3
    for i in range(3):
        for j in range(3):
            if board[start_y+i][start_x+j] == val:
                return True
    return False

def dfs(idx):
    if idx == len(zeros):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=' ')
            print('')
        exit(0)
    x, y = zeros[idx]
    for i in range(1, 10):
        if not is_duplicated_x(y, i) and not is_duplicated_y(x, i) and not is_duplicated_square(x, y, i):
            board[y][x] = i
            dfs(idx+1)
            board[y][x] = 0
# print('----------------')
dfs(0)
