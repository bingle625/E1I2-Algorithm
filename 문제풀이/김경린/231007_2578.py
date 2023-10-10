board = []
command = []
pos = {}
for i in range(5):
    tmp = input().split(' ')
    board.append(tmp)
    for j in range(5):
        pos[tmp[j]] = (j,i)
for i in range(5):
        tmp = input().split(' ')
        command.append(tmp)

def is_bingo(board, j, i):
    cnt = 0
    bingo = True
    for y in range(5):
        if board[y][i] != '0':
            bingo = False             
            break
    if bingo:
        cnt += 1


    bingo = True
    for x in range(5):
        if board[j][x] != '0':
            bingo = False
            break
    if bingo:
        cnt += 1
    
    if i == j:
        bingo = True
        for z in range(5):
            if board[z][z] != '0':
                bingo = False
                break
        if bingo:
            cnt += 1
    
    if i+j == 4:
        bingo = True
        for z in range(5):
            if board[4-z][z] != '0':
                bingo = False
                break
        if bingo:
            cnt += 1



    return cnt 



def solution(board):
    cnt = 0
    for i in range(5):
        for j in range(5):
            x, y = pos[command[i][j]]
            board[y][x] = '0'
            cnt += is_bingo(board, y, x)
            if cnt >= 3:
                return i*5+j+1

print(solution(board))

