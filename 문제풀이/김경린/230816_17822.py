from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m, t = map(int, input().split(' '))

board = []
cnt = n*m

def rotate(board, dir, k):
    # 시계
    if dir == 0:
        for i in range(k):
            board.appendleft(board.pop())
    # 반시계
    else:
        for i in range(k):
            board.append(board.popleft())
    return board

def erase(board):
    global cnt
    visited = [[0 for _ in range(m)] for _ in range(n)]
    is_erase = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and board[i][j]!=0:
                visited[i][j] = 1
                q = deque()
                for dir in range(4):
                    next_x = (j + dx[dir])%m
                    next_y = i + dy[dir]
                    if 0<=next_x<m and 0<=next_y<n and visited[next_y][next_x] == 0 and board[next_y][next_x] == board[i][j]:
                        q.append((next_x, next_y))
                        visited[next_y][next_x] = 1
                        is_erase = 1
                if len(q) > 0:
                    board[i][j] = 0
                    cnt -= 1

                while len(q):
                    x, y = q.popleft()
                    for dir in range(4):
                        next_x = (x + dx[dir])%m
                        next_y = y + dy[dir]
                        if 0<=next_x<m and 0<=next_y<n and visited[next_y][next_x] == 0 and board[next_y][next_x] == board[y][x]:
                            is_erase = 1
                            q.append((next_x, next_y))
                            visited[next_y][next_x] = 1
                    board[y][x] = 0
                    cnt -= 1
            
    return is_erase
        




for i in range(n):
    tmp = deque(map(int, input().split(' ')))
    board.append(tmp)

for i in range(t):
    x, dir, k = map(int, input().split(' '))

    for j in range(n):
        if (j+1)%x == 0:
            board[j] = rotate(board[j], dir, k)
    is_erase = erase(board)
    if not is_erase:
        # 평균을 구하고, 평균보다 큰수에는 1 빼고 작은수는 1 더하기
        sum_board = 0
        for b in board:
            sum_board += sum(b)
        
        if sum_board == 0:
            break

        avg = sum_board / cnt

        for i in range(n):
            for j in range(m):
                if board[i][j] != 0:
                    if board[i][j] > avg:
                        board[i][j] -= 1
                    elif board[i][j] < avg:
                        board[i][j] += 1

sum_board = 0
for b in board:
    sum_board += sum(b)

print(sum_board)
