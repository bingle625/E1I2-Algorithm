# 누적합 문제
# 주어진 범위에 숫자를 더하는 것 -> 매번 더하지 않고 경계 부분을 표시하여 누적합으로 최종적으로 더할 수를 구함
def solution(board, skill):
    answer = 0
    board_ = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    for t, y1,x1,y2,x2,degree in skill:
        board_[y1][x1] += (t*2-3)*degree
        board_[y1][x2+1] -= (t*2-3)*degree # 오른쪽으로는 더하지 않는다
        board_[y2+1][x1] -= (t*2-3)*degree # 밑으로는 더하지 않는다
        board_[y2+1][x2+1] += (t*2-3)*degree # 위에서 공통된 범위의 -가 있기 때문에 더해줌
    
    for i in range(1, len(board_[0])):
        board_[0][i] += board_[0][i-1] 
    for i in range(1, len(board_)):
        board_[i][0] += board_[i-1][0]
    
    for i in range(1, len(board_)):
        for j in range(1, len(board_[0])):
            board_[i][j] += board_[i-1][j] + board_[i][j-1] - board_[i-1][j-1]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]+board_[i][j] > 0:
                answer += 1
        

    return answer