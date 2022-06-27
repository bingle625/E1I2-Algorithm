

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
                test.append((tmp_m, tmp_n))
                selectBlock(idx+1,num-1)
                board[tmp_n][tmp_m]=0
        else:
            print(test)
            break
        idx += 1
        if idx >= n*m:
            break
        


while True:
    selectBlock(0,3)

