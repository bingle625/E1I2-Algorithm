# 체스판 다시 칠하기
ideal_B = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
]

ideal_W = [
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1]
]


def chess_min(board, min):
    cnt = 0
    end = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != ideal_B[i][j]:
                cnt += 1
                if cnt > min:
                    end = 1
                    break
        if end == 1:
            break
    if end == 0:
        min = cnt

    end = 0
    cnt = 0

    for i in range(8):
        for j in range(8):
            if board[i][j] != ideal_W[i][j]:
                cnt += 1
                if cnt > min:
                    end = 1
                    break
        if end == 1:
            break

    if end == 0:
        min = cnt

    return min


height, width = input().split()
height = int(height)
width = int(width)

board = [[0 for _ in range(width)] for _ in range(height)]

for i in range(height):
    tmp = input()
    for k in range(width):
        if tmp[k] == 'W':
            board[i][k] = 1
        elif tmp[k] == 'B':
            board[i][k] = 0

min = 2500

for i in range(height-7):
    for j in range(width-7):
        new_board = [[board[0+i+l][0+j+k] for k in range(8)] for l in range(8)]
        min = chess_min(new_board, min)

print(min)
