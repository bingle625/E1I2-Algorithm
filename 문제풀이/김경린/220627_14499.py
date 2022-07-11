

n, m = map(int, input().split(' '))


board = [] 
for k in range(n):
    board.append(list(map(int, input().split())))

test = []
def selectBlock(idx,num):
    while True:
        if num != 0: 
            tmp_m = idx % m
            tmp_n = idx // m
            if board[tmp_n][tmp_m]==0:
                board[tmp_n][tmp_m]=1
                selectBlock(idx+1,num-1)
                board[tmp_n][tmp_m]=0

            idx += 1
            if idx >= n*m:
                break
        else:
            break

        


while True:
    selectBlock(0,3)

