red = [[0 for _ in range(4)] for _ in range(4)]
blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]

score = 0

def copy_col(board, from_j, to_j):
    for i in range(4):
        board[i][to_j] = board[i][from_j]

def get_col(board, j):
    answer = []
    for i in range(4):
        answer.append(board[i][j])
    return answer

def move(board, is_green, k):
    if is_green:
        for i in range(k, 0, -1):
            if board[i] == [0, 0, 0, 0]:
                return 
            board[i] = board[i-1][:]
        board[0] = [0, 0, 0, 0]
    else:
        for j in range(k, 0, -1):
            if get_col(board, j) == [0, 0, 0, 0]:
                return
            copy_col(board, j-1, j)
        
        for i in range(4):
            board[i][0] = 0
    return

    
    

def put_green(blocks, green):
    global score
    x = blocks[0][0]
    x_length = 1
    y_length = 1
    if len(blocks) == 2:
        if blocks[0][0] != blocks[1][0]:
            x_length = 2
        else:
            y_length = 2
    fin = False
    for i in range(5):
        for j in range(x, x+x_length):
            if green[i+1][j] != 0:
                for k in range(x, x+x_length):
                    green[i][k] = 1
                if y_length == 2:
                    green[i-1][x] = 1
                fin = True
                break
        if fin:
            break

    if not fin:
        for j in range(x,x+x_length):
            green[5][j] = 1
        if y_length == 2:
            green[4][x] = 1
    
    # 점수 계산
    is_score = True
    while is_score:
        is_score = False
        for i in range(2, 6):
            if green[i][:] == [1,1,1,1]:
                is_score = True
                score += 1
                move(green, True, i)
            
                
    
    return


def put_blue(blocks, blue):
    global score
    y = blocks[0][1]
    y_length = 1
    x_length = 1
    if len(blocks) == 2:
        if blocks[0][1] != blocks[1][1]:
            y_length = 2
        else:
            x_length = 2
    
    fin = False
    for j in range(5):
        for i in range(y, y+y_length):
            if blue[i][j+1] != 0:
                for k in range(y, y+y_length):
                    blue[k][j] = 1
                if x_length == 2:
                    blue[y][j-1] = 1
                fin = True
        if fin:
            break
    if not fin:
        for i in range(y,y+y_length):
            blue[i][5] = 1
        if x_length == 2:
            blue[y][4] = 1
        

    # 점수 계산
    is_score = True
    while is_score:
        is_score = False
        for j in range(2, 6):
            if get_col(blue, j) == [1,1,1,1]:
                is_score = True
                score += 1
                move(blue, False, j)
    return

def calc_special(board, is_green):
    if is_green:
        cnt = 0
        for i in range(1, -1, -1):
            for j in range(4):
                if board[i][j] == 1:
                    cnt += 1
                    break
        for _ in range(cnt):
            move(board, True, 5)
    else:
        cnt = 0
        for j in range(1, -1, -1):
            for i in range(4):
                if board[i][j] == 1:
                    cnt += 1
                    break

        for _ in range(cnt):
            move(board, False, 5)




def put_block(t, x, y, green, blue):
    blocks = []
    if t == 1:
        blocks.append((x,y))

    elif t == 2:
        blocks.append((x,y))
        blocks.append((x+1, y))


    elif t == 3:
        blocks.append((x,y))
        blocks.append((x, y+1))
    
    # 블록 떨어트리기
    put_green(blocks, green)
    put_blue(blocks, blue)

    # 특별구역 계산
    calc_special(green, True)
    calc_special(blue, False)


    
    



n = int(input())
for i in range(n):
    t, y, x = map(int, input().split(' '))

    put_block(t, x, y, green, blue)
    # print(score)
    # print(green)
    # print(blue)

print(score)
cnt = 0
for i in range(6):
    for j in range(4):
        if green[i][j] == 1:
            cnt += 1

for i in range(4):
    for j in range(6):
        if blue[i][j] == 1:
            cnt += 1
print(cnt)