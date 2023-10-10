import copy


dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

board = [[] for _ in range(4)]
fishes = [(0, 0) for _ in range(17)]

for i in range(4):
    tmp = list(map(int, input().split(' ')))
    for j in range(4):
        board[i].append([tmp[2*j], tmp[2*j+1] - 1])
        fishes[tmp[2*j]] = (j, i)



max_score = 0


# board = [[물고기 번호, 방향]] 빈 공간 [-1,-1] 상어 [0, pos]
# fishes = [(x, y)]

def move_fish(board, fishes):
    for i in range(1, 17):
        if len(fishes[i]) > 0:
            x, y = fishes[i][0], fishes[i][1]
            pos = board[y][x][1]
            for j in range(8):
                next_x = x + dx[(pos+j)%8]
                next_y = y + dy[(pos+j)%8]
                if (0<=next_x<4 and 0<=next_y<4) and board[next_y][next_x][0] != 0:
                    changed_fish_num, changed_fish_pos = board[next_y][next_x][0], board[next_y][next_x][1]
                    board[next_y][next_x] = (i, (pos+j)%8)
                    fishes[i] = (next_x, next_y)
                
                    board[y][x] = [changed_fish_num, changed_fish_pos]
                    if changed_fish_num != -1:
                        fishes[changed_fish_num] = (x,y)
                    break



def move_shark(board, fishes, shark_x, shark_y, pos, score):
    global max_score
    i = 1
    while True:
        next_x = shark_x + dx[pos]*i
        next_y = shark_y + dy[pos]*i
        if 0<=next_x<4 and 0<=next_y<4: 
            if board[next_y][next_x] == [-1, -1]:
                i += 1
                continue
            origin_board = copy.deepcopy(board)
            origin_fishes = copy.deepcopy(fishes)
            new_fish = board[next_y][next_x][0]
            new_pos = board[next_y][next_x][1]
            board[shark_y][shark_x] = [-1, -1]
            fishes[new_fish] = ()
            board[next_y][next_x] = [0, new_pos] # 상어는 idx 0
            move_fish(board, fishes)
            move_shark(board, fishes, next_x, next_y, new_pos, score + new_fish)
            
            board = origin_board
            fishes = origin_fishes
        else:
            break
        i += 1
    max_score = max(score, max_score)

shark_x = 0
shark_y = 0
pos = board[0][0][1]
score = board[0][0][0]
board[0][0] = [0, pos]
fishes[score] = ()
move_fish(board, fishes)
move_shark(board, fishes, shark_x, shark_y, pos, score)
print(max_score)
