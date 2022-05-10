from collections import deque
from sys import stdin

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# index가 증가하는 것은 오른쪽 감소하는 것은 왼쪽

#사과는 . 비어있는 곳은 0 뱀은* board테두리는 1

size = int(stdin.readline())

board = [[0 for _ in range(size+2)] for _ in range(size+2)]

for i in range(size+2):
    board[0][i] = 1
    board[size+1][i] = 1
    board[i][0] = 1
    board[i][size+1] = 1

board[1][1] = '*'
snake = deque()
snake.append([1,1])
    
appleNum = int(stdin.readline().rstrip())
for i in range(appleNum):
    row,col = map(int, stdin.readline().split())
    board[row][col] = '.'

turn = int(stdin.readline())
change = deque()
for i in range(turn):
    time, direction = stdin.readline().split()
    time = int(time)
    change.append([time, direction])

def move(board, snake, dX, dY):
    head = snake[0]
    col = head[1] + dX
    row = head[0] + dY
    if board[row][col] == 1 or board[row][col] == '*':
        return 0
    elif board[row][col]=='.':
        board[row][col] = '*'
        snake.appendleft([row,col])
        return 1
    else:
        tail = snake.pop()
        board[tail[0]][tail[1]] = 0
        board[row][col] = '*'
        snake.appendleft([row,col])
        return 1, [row, col], tail

time = 0


n = 0

while True:
    time += 1
    if change and change[0][0]+1 == time:
        cTime, cDirect = change.popleft()
        if cDirect=='D':
            n = (n+1)%4
        else:
            n = (n-1)%4 if n >= 1  else 3
    done = move(board, snake, dx[n], dy[n])
    
    if done == 0:
            print(time)
            break
    
    # for i in range(size+2):
    #     for j in range(size+2):
            
    #         board[i][j] = str(board[i][j])
        
    #     print(''.join(board[i]))

    # print(time)
    # print('========================================================\n\n')


