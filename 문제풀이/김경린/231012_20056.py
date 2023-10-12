from collections import deque
import math

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m, k = map(int, input().split(' '))

board = [[ deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    y, x, m, s, d = map(int, input().split(' '))
    y -= 1
    x -= 1
    board[y][x].append([m,s,d,False])


def calc_pos(pos):
    if pos < 0:
        while pos + n < 0:
            pos += n
        return pos + n
    elif pos >= n:
        return pos%n
    else:
        return pos

def move(board):
    for i in range(n):
        for j in range(n):
            length = len(board[i][j])
            for idx in range(length):
                m, s, d, is_calc = board[i][j][0]
                
                if is_calc == False:
                    board[i][j].popleft()
                    next_x = calc_pos(j + dx[d]*s)
                    next_y = calc_pos(i + dy[d]*s)
                    # print(j, i, d, s, j + dx[d]*s, i + dy[d]*s, next_x, next_y)
                    
                    board[next_y][next_x].append([m, s, d, True])
                else:
                    break

def calc_fireball(board):
    for i in range(n):
        for j in range(n):
            length = len(board[i][j])
            if length > 1:
                sum_m, sum_s = 0, 0
                is_all_even_or_odd = True
                divided = board[i][j][0][2] % 2
                for idx in range(len(board[i][j])):
                    sum_m += board[i][j][idx][0]
                    sum_s += board[i][j][idx][1]
                    if divided != (board[i][j][idx][2] % 2):
                        is_all_even_or_odd = False
                sum_m = math.floor(sum_m / 5)
                sum_s = math.floor(sum_s / length)
                if is_all_even_or_odd:
                    d = [0, 2, 4, 6]
                else:
                    d = [1, 3, 5, 7]
    
                board[i][j] = deque()
                if sum_m > 0:
                    for dir in range(4):
                        board[i][j].append([sum_m, sum_s, d[dir], False])
            elif length == 1:
                board[i][j][0][3] = False

def calc_m(board):
    sum_m = 0
    for i in range(n):
        for j in range(n):
            for b in range(len(board[i][j])):
                sum_m += board[i][j][b][0]
    return sum_m

def print_board(board):
    for b in board:
        print(b)
    print('---------')

for _ in range(k):
    move(board)
    # print_board(board)
    calc_fireball(board)
    # print_board(board)


print(calc_m(board))

                



