from collections import defaultdict


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split(' '))
board = []
for i in range(n):
    tmp = list(map(int, input().split(' ')))
    board.append(tmp)

figures = []
board_figures = defaultdict(list)

for i in range(k):
    y, x, dir = map(int, input().split(' '))
    x -= 1
    y -= 1
    dir -= 1
    figures.append([x, y, dir])
    board_figures[(x,y)].append(i)

def move(x, y, i, next_x, next_y, moving, board_figures, figures):
        # if board_figures[(x,y)][i] == f_idx:
        #     moving = board_figures[(x,y)][i:]
    board_figures[(x,y)] = board_figures[(x,y)][0:i]
            # moving.reverse()
    board_figures[(next_x, next_y)] += moving

    for m in moving:
        figures[m][0] = next_x
        figures[m][1] = next_y

def game(board, figures, board_figures):
    for f_idx in range(k):
        x, y, dir = figures[f_idx]
        next_x = x + dx[dir]
        next_y = y + dy[dir]

        if 0<= next_x <n and 0<=next_y<n:
            # 빨간색
            if board[next_y][next_x] == 1:
                for i in range(len(board_figures[(x,y)])):
                    if board_figures[(x,y)][i] == f_idx:
                        moving = board_figures[(x,y)][i:]
                        # print('moving',moving)
                        # print('f_idx', f_idx)
                        moving.reverse()
                        move(x, y, i, next_x, next_y, moving, board_figures, figures)
                        break

            # 파란색
            elif board[next_y][next_x] == 2:
                if dir == 0:
                    next_x = x + dx[1]
                    figures[f_idx][2] = 1
                elif dir == 1:
                    next_x = x + dx[0]
                    figures[f_idx][2] = 0
                elif dir == 2:
                    next_y = y + dy[3]
                    figures[f_idx][2] = 3
                elif dir == 3:
                    next_y = y + dy[2]
                    figures[f_idx][2] = 2
                if 0<=next_x<n and 0<=next_y<n and board[next_y][next_x] != 2:
                    for i in range(len(board_figures[(x,y)])):
                        if board_figures[(x,y)][i] == f_idx:
                            moving = board_figures[(x,y)][i:]
                            if board[next_y][next_x] == 1:
                                moving.reverse()
                            # print('moving',moving)
                            # print('f_idx', f_idx)
                            move(x, y, i, next_x, next_y, moving, board_figures, figures)
                            break
            # 흰색
            else:
                for i in range(len(board_figures[(x,y)])):
                    if board_figures[(x,y)][i] == f_idx:
                        moving = board_figures[(x,y)][i:]
                        move(x, y, i, next_x, next_y, moving, board_figures, figures)
                        break

        else:
            #파란색과 같은 결과
            if dir == 0:
                next_x = x + dx[1]
                figures[f_idx][2] = 1
            elif dir == 1:
                next_x = x + dx[0]
                figures[f_idx][2] = 0
            elif dir == 2:
                next_y = y + dy[3]
                figures[f_idx][2] = 3
            elif dir == 3:
                next_y = y + dy[2]
                figures[f_idx][2] = 2
            
            if 0<=next_x<n and 0<=next_y<n and board[next_y][next_x] != 2:
                for i in range(len(board_figures[(x,y)])):
                    if board_figures[(x,y)][i] == f_idx:
                        moving = board_figures[(x,y)][i:]
                        if board[next_y][next_x] == 1:
                            moving.reverse()
                        move(x, y, i, next_x, next_y, moving, board_figures, figures)
                        break
        if len(board_figures[(next_x, next_y)]) >= 4:
            return True
    return False

cnt = 0
while cnt <= 1000:
    if game(board, figures, board_figures):
        # 게임이 끝난 경우
        print(cnt+1)
        break
    else:
        cnt += 1
    
if cnt > 1000:
    print(-1)

