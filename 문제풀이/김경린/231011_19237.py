from collections import defaultdict, deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n,  m , k = map(int, input().split(' '))

board = [[[] for _ in range(n)] for _ in range(n)] # 상어 번호, 남은 냄새
sharks = defaultdict(deque) # 현재 위치 x, y, 방향
sharks_direction = [[] for _ in range(m+1)]
# 상어 idx는 그대로 방향은 idx-1
is_out = [ False for _ in range(m+1)]


for i in range(n):
    tmp = list(map(int, input().split(' ')))
    for j in range(n):
        if tmp[j] != 0:
            board[i][j] = [tmp[j], k]
            sharks[tmp[j]].append([j, i])

sharks_dir = list(map(int, input().split(' ')))
for i in range(1, m+1):
    sharks[i][0].append(sharks_dir[i-1])

for i in range(1, m+1):
    for j in range(4):
        tmp = list(map(int, input().split(' ')))
        sharks_direction[i].append(tmp)

def remove_smell(sharks, board):
    for i in range(1, m+1):
        while len(sharks[i]):
            x, y = sharks[i][0][0], sharks[i][0][1]
            if board[y][x][1] == 1:
                sharks[i].popleft()
                board[y][x] = []
            else:                
                break
        for j in range(len(sharks[i])):
            x, y = sharks[i][j][0], sharks[i][j][1]         
            board[y][x][1] -= 1


def move(board, sharks, is_out):
    next_moves = []
    for i in range(1, m+1):
        is_move = False
        is_mine = False
        if len(sharks[i]) and not is_out[i]:
            x, y, dir = sharks[i][-1][0], sharks[i][-1][1], sharks[i][-1][2]
            dir -= 1
            for d in sharks_direction[i][dir]:
                next_x = x + dx[d-1]
                next_y = y + dy[d-1]
                if 0<=next_x<n and 0<=next_y<n:
                        # 이동 가능한 경우
                    if len(board[next_y][next_x]) == 0:
                        next_x, next_y, next_dir = next_x, next_y, d
                        next_moves.append([i, next_x, next_y, next_dir])
                        is_move = True
                        break
                    else:

                        # 냄새가 있는 경우
                            if is_mine == False and board[next_y][next_x][0] == i:
                                is_mine = True
                                done_x, done_y, done_dir = next_x, next_y, d
                            continue
            if not is_move and is_mine:
                next_moves.append([i, done_x, done_y, done_dir])

    for i, next_x, next_y, dir in next_moves:
        if len(board[next_y][next_x]) > 0: 
            if board[next_y][next_x][0] == i:
                board[next_y][next_x] = [i, k+1]
                # print(sharks[i])
                for idx in range(len(sharks[i])):
                    if sharks[i][idx][0] == next_x and sharks[i][idx][1] == next_y:
                        done_idx = idx
                        break 
                        
                sharks[i].remove([sharks[i][done_idx][0],  sharks[i][done_idx][1],  sharks[i][done_idx][2]])
                sharks[i].append([next_x, next_y, dir])
            else:
                is_out[i] = True
                continue

        else:
            board[next_y][next_x] = [i, k+1]
            sharks[i].append([next_x, next_y, dir])




def is_shark1_remain_only(is_out):
    for i in range(2, m+1):
        if is_out[i] == False:
            return False
    
    return True


t = 0
while not is_shark1_remain_only(is_out) and t <= 1000:
    
    # 상어 움직임
    move(board, sharks, is_out)
    remove_smell(sharks, board)

    t += 1

print(t if t <= 1000 else -1)

        



