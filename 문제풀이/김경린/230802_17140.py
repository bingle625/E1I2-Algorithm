# transpose 함수 zip

from typing import Counter

def row__bigger_than_col(board):
    return True if len(board) >= len(board[0]) else False


def cal_r(board):
    new_board = []
    max_row = 0
    for i in range(len(board)):
        cnt_dict = Counter(board[i])
        cnt_dict = sorted(cnt_dict.items(), key=lambda x:(x[1],x[0]))
        cnt_list = []
        for key, val in cnt_dict:
            if key != 0:
                cnt_list.append(key)
                cnt_list.append(val)
        
        if len(cnt_list) > 100:
            cnt_list = cnt_list[:100]
        
        max_row = max(len(cnt_list), max_row)
        new_board.append(cnt_list)
    
    for i in range(len(new_board)):
        for j in range(len(new_board[i]), max_row):
            new_board[i].append(0)
    
    return new_board
    

def cal_c(board):
    new_board = cal_r(list(map(list,zip(*board))))
    return list(map(list,zip(*new_board)))
    # new_board = []
    # max_col = 0
    # for i in range(len(board[0])):
    #     cnt_dict = Counter([board[j][i] for j in range(len(board))])
    #     cnt_dict = sorted(cnt_dict.items(), key=lambda x:(x[1],x[0]))
    #     cnt_list = []
    #     for key, val in cnt_dict:
    #         if key != 0:
    #             cnt_list.append(key)
    #             cnt_list.append(val)
        
    #     if len(cnt_list) > 100:
    #         cnt_list = cnt_list[:100]

    #     max_col = max(len(cnt_list), max_col)
    #     new_board.append(cnt_list)
    # new_board_reverse = [[]for _ in range(max_col)]
    # for i in range(len(new_board)):
    #     for j in range(len(new_board[i])):
    #         new_board_reverse[j].append(new_board[i][j])
    #     for j in range(len(new_board[i]), max_col):
    #         new_board_reverse[j].append(0)
    
    return new_board_reverse



r, c, k = map(int, input().split(' ')) 
r -= 1
c -= 1

board = []
for i in range(3):
    tmp = list(map(int, input().split(' ')))
    board.append(tmp)

t = 0
while True:
    if len(board) > r and len(board[0]) > c and board[r][c] == k:
        break
    if t > 100:
        t = -1
        break
    if row__bigger_than_col(board):
        board = cal_r(board)
    else:
        board = cal_c(board)
    t += 1

print(t)