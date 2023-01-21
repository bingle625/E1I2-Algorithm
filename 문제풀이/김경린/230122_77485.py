
# def turn(query, board):
#     y1, x1, y2, x2 = query[0]-1,query[1]-1,query[2]-1,query[3]-1

#     board_copy = []
#     for i in range(y1, y2+1):
#         board_copy.append(board[i][x1:x2+1])
#     # l_up, r_up, r_down, l_down = board[y1][x1], board[y1][x2], board[y2][x2], board[y2][x1]
#     min_num = board[y1][x1]
#     # 북
#     for x in range(x1+1, x2+1):
#         min_num = min(min_num, board[y1][x])
#         board[y1][x] = board_copy[0][x-1-x1]
#     # 동
#     for y in range(y1+1, y2+1):
#         min_num = min(min_num, board[y][x2])
#         board[y][x2] = board_copy[y-1-y1][x2-x1]
#     # 남
#     for x in range(x1, x2):
#         min_num = min(min_num, board[y2][x])
#         board[y2][x] = board_copy[y2-y1][x+1-x1]
#     # 서
#     for y in range(y1, y2):
#         min_num = min(min_num, board[y][x1])
#         board[y][x1] = board_copy[y+1-y1][0]
#     return min_num
    
            
# def solution(rows, columns, queries):
#     answer = []
#     board = [ [ j*columns + i+1 for i in range(columns)] for j in range(rows)]
#     for query in queries:
#         answer.append(turn(query, board))
    
#     return answer


# 행렬 돌리기 stack 풀이!

def turn(query, board):
    y1, x1, y2, x2 = query[0]-1,query[1]-1,query[2]-1,query[3]-1

    min_num = board[y1][x1]
    stack = []
    # 북
    for x in range(x1, x2+1):
        stack.append(board[y1][x])
        if len(stack) == 1:
            continue
        else:
            board[y1][x] = stack[-2]
    # 동
    for y in range(y1+1, y2+1):
        stack.append(board[y][x2])
        board[y][x2] = stack[-2]
    # 남
    for x in range(x2-1, x1-1, -1):
        stack.append(board[y2][x])
        board[y2][x] = stack[-2]
    # 서
    for y in range(y2-1, y1-1, -1):
        stack.append(board[y][x1])
        board[y][x1] = stack[-2]
    return min(stack)
    
            
def solution(rows, columns, queries):
    answer = []
    board = [ [ j*columns + i+1 for i in range(columns)] for j in range(rows)]
    for query in queries:
        answer.append(turn(query, board))
    
    return answer