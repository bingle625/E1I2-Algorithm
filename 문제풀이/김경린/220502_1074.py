
N, row, col = map(int,input().split())
def cal_visit(N,row,col):
    time = 0
    if N == 1:
        return row*2 + col
    if row >= 2**(N-1):
        time += 2

    if col >= 2**(N-1):
        time += 1
    
    result = 2**(2*N-2)*time +cal_visit(N-1 ,row if row<2**(N-1) else row - 2**(N-1), col if col<2**(N-1) else col - 2**(N-1) )
    return result


print(cal_visit(N,row,col))