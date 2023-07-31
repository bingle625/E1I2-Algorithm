dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m, t = map(int, input().split(' '))

board = []
air_cleaner = []
for i in range(n):
    tmp = list(map(int, input().split(' ')))
    for j in range(m):
        if tmp[j] == -1:
            air_cleaner.append(i)
    board.append(tmp)

def spread():
    global board
    spread_board = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            spread_cnt = 0
            if board[i][j] > 0:
                for dir in range(4):
                    next_x = j + dx[dir]
                    next_y = i + dy[dir]
                    if 0 <= next_x < m and 0 <= next_y < n and board[next_y][next_x] != -1:
                        spread_board[next_y][next_x] += board[i][j]//5
                        spread_cnt += 1
                board[i][j] -= board[i][j]//5*spread_cnt
    
    for i in range(n):
        for j in range(m):
            board[i][j] += spread_board[i][j]

def circulate():
    global board
    air_cleaner.sort()
    # 위쪽 공기청정기
    up_y = air_cleaner[0]
    last = 0
    for x in range(1, m):
        cur = board[up_y][x]
        board[up_y][x] = last
        last = cur  
    
    for y in range(up_y-1, -1, -1):
        cur = board[y][m-1]
        board[y][m-1] = last
        last = cur 
    
    for x in range(m-2, -1, -1):
        cur = board[0][x]
        board[0][x] = last
        last = cur
    
    for y in range(1, up_y):
        cur = board[y][0]
        board[y][0] = last
        last = cur
  
    # 아래 공기청정기
    down_y = air_cleaner[1]
    last = 0
    for x in range(1, m):
        cur = board[down_y][x]
        board[down_y][x] = last
        last = cur  
    
    for y in range(down_y+1, n):
        cur = board[y][m-1]
        board[y][m-1] = last
        last = cur 
    
    for x in range(m-2, -1, -1):
        cur = board[n-1][x]
        board[n-1][x] = last
        last = cur
    
    for y in range(n-2, down_y, -1):
        cur = board[y][0]
        board[y][0] = last
        last = cur
    



answer = 0
for i in range(t):
    spread()
    # print(board)
    circulate()
    # print(board)
for b in board:
    answer += sum(b)
    
print(answer+2)
