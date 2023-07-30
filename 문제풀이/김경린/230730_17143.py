from collections import deque
from copy import deepcopy


n, m, shark_num = map(int, input().split(' '))

# s 속력, d 이동 방향, z 크기

board = [[[] for _ in range(m)] for _ in range(n)]
for i in range(shark_num):
    r,c,s,d,z = map(int, input().split(' '))
    r -= 1
    c -= 1
    board[r][c] = [s, d, z]


fishing_size = 0
for i in range(m):
    new_board = [[[] for _ in range(m)] for _ in range(n)]

    # 낚시
    for j in range(n):
        if len(board[j][i]) > 0:
            fishing_size += board[j][i][2]
            board[j][i] = []
            break
    
    #이동
    for y in range(n):
        for x in range(m):
            if len(board[y][x])>0:
                new_x = x
                new_y = y
                s, d, z = board[y][x]
                # 위
                if d == 1:
                    if y - s < 0:
                        dif = abs(y-s)
                        if (dif//(n-1)) % 2 == 0:
                            d = 2
                            new_y = dif % (n-1)
                        else:
                            new_y = n-1 - (dif % (n-1))
                    else:
                        new_y = y - s            
                # 아래
                elif d == 2:
                    if ((y + s) // (n-1)) % 2 == 0:
                        new_y = (y + s)%(n-1)
                    else:
                        d = 1
                        new_y = n-1-(y+s)%(n-1)
                # 오른쪽
                elif d == 3:
                    if ((x + s) // (m-1)) % 2 == 0:
                        new_x = (x + s)%(m-1)
                    else:
                        d = 4
                        new_x = m-1-(x+s)%(m-1)
                # 왼쪽
                elif d == 4:
                    if x - s < 0:
                        dif = abs(x-s)
                        if (dif//(m-1)) % 2 == 0:
                            d = 3
                            new_x = dif % (m-1)
                        else:
                            new_x = m-1 - (dif % (m-1))
                    else:
                        new_x = x - s

                # 한 칸에 두마리 이상 상어 검사
                if len(new_board[new_y][new_x]) > 0:
                    if z > new_board[new_y][new_x][2]:
                        new_board[new_y][new_x] = [s, d, z]
                else:
                    new_board[new_y][new_x] = [s, d, z]

    board = deepcopy(new_board)

print(fishing_size)