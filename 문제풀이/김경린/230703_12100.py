from collections import deque
from copy import deepcopy

max_num = 0

def move(board, dir, n, depth):
    global max_num

    
    if dir == 0:
        for i in range(n):
            tmp = deque()
            board[i] = deque([ c for c in board[i] if c != 0 ])
            while len(board[i]) > 1:
                top = board[i].pop()
                if top == board[i][-1]:
                    top2 = board[i].pop()
                    tmp.appendleft(top+top2)
                else:
                    tmp.appendleft(top)
            while len(board[i]) > 0:
                tmp.appendleft(board[i].pop())
            
            while len(tmp) != n:
                tmp.appendleft(0)
            board[i] = tmp
        
    
    elif dir == 1:
        for i in range(n):
            tmp = deque()
            board_row = deque([ board[j][i] for j in range(n) if board[j][i] != 0 ])
            while len(board_row) > 1:
                top = board_row.pop()
                if top == board_row[-1]:
                    top2 = board_row.pop()
                    tmp.appendleft(top+top2)
                else:
                    tmp.appendleft(top)
            while len(board_row) > 0:
                tmp.appendleft(board_row.pop())
            
            while len(tmp) != n:
                tmp.appendleft(0)
            
            for j in range(n):
                board[j][i] = tmp[j]

    elif dir == 2:
        for i in range(n):
            tmp = deque()
            board[i] = deque([ c for c in board[i] if c != 0 ])
            while len(board[i]) > 1:
                top = board[i].popleft()
                if top == board[i][0]:
                    top2 = board[i].popleft()
                    tmp.append(top+top2)
                else:
                    tmp.append(top)
            while len(board[i]) > 0:
                tmp.append(board[i].pop())
            
            while len(tmp) != n:
                tmp.append(0)
            board[i] = tmp
    elif dir == 3:
        for i in range(n):
            tmp = deque()
            board_row = deque([ board[j][i] for j in range(n) if board[j][i] != 0 ])
            while len(board_row) > 1:
                top = board_row.popleft()
                if top == board_row[0]:
                    top2 = board_row.popleft()
                    tmp.append(top+top2)
                else:
                    tmp.append(top)
            while len(board_row) > 0:
                tmp.append(board_row.pop())
            
            while len(tmp) != n:
                tmp.append(0)
            
            for j in range(n):
                board[j][i] = tmp[j]
            
    for j in range(4):
        if depth == 4:
            for i in range(n):
                max_num = max(max_num, max(board[i]))
            return 
        else:
            board_tmp = deepcopy(board)  
            move(board_tmp, j, n, depth+1)

cnt = int(input())

board = []
for i in range(cnt):
    tmp = list(map(int, input().split(' ')))
    board.append(tmp)


for j in range(4):
    board_tmp = deepcopy(board)  
    move(board_tmp, j, cnt, 0)

print(max_num)