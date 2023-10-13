from collections import deque

n, q = map(int, input().split(' '))
n = 2**n

dx = [1,0,-1,0]
dy = [0,1,0,-1]

board = []
for _ in range(n):
    tmp = list(map(int, input().split(' ')))
    board.append(tmp)

ls = list(map(int, input().split(' ')))

def print_board():
    for b in board:
        print(b)
    print('--------------')

def turn(board, x_start, x_finish, y_start, y_finish):
    # print(x_start, x_finish, y_start, y_finish)
    up = board[y_start][x_start:x_finish+1]
    down = board[y_finish][x_start:x_finish+1]
    right = []
    left = []
    for y in range(y_start, y_finish+1):
        right.append(board[y][x_finish])
        left.append(board[y][x_start])
    right = right[::-1]
    left = left[::-1]

    board[y_start][x_start:x_finish+1] = left
    board[y_finish][x_start:x_finish+1] = right

    for y in range(y_start, y_finish+1):
        board[y][x_finish] = up[y-y_start]
        board[y][x_start] = down[y-y_start]

def magic(board, j):
    
    for y in range(n//j):
        for x in range(n//j):
            x_start = j*x
            x_finish = j*(x+1)-1
            y_start = j*y
            y_finish = j*(y+1)-1
            for k in range(j//2):
                turn(board, x_start+k, x_finish-k, y_start+k,y_finish-k)
            
def remove(board):
    deleted = []
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                cnt = 0
                for k in range(4):
                    next_x = j + dx[k]
                    next_y = i + dy[k]
                    if 0 <= next_x < n and 0<=next_y<n and board[next_y][next_x] > 0:
                        cnt += 1
                        if cnt >= 3:
                            break
                if cnt < 3:
                    deleted.append([j,i])
    for x, y in deleted:
        board[y][x] -= 1

def sum_ice():
    cnt = 0
    for b in board:
        cnt += sum(b)
    return cnt

def bfs():
    visited = [[0 for _ in range(n)] for _ in range(n)]
    max_cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] > 0:
                cnt = 0
                deq = deque()
                deq.append([j, i])
                visited[i][j] = 1
                while len(deq):
                    x, y = deq.popleft()
                    cnt += 1
                    for k in range(4):
                        next_x = x + dx[k]
                        next_y = y + dy[k]
                        if 0 <= next_x < n and 0<=next_y<n and board[next_y][next_x] > 0 and not visited[next_y][next_x]:
                            visited[next_y][next_x] = 1
                            deq.append([next_x, next_y])
                max_cnt = max(cnt, max_cnt)
    return max_cnt
                


for i in range(1, q+1):
    j = 2**ls[i-1]
    magic(board, j)
    remove(board)

ice = sum_ice()
print(ice)
max_ice = bfs()
print(max_ice)


