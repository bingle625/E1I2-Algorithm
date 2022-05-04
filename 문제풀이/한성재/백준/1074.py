# 1074번 Z

def getOrder(N,r,c):
    if N == 0:
        return 0
    
    if r == 0:
        row = 2**N
    else:
        row = r
    
    if c == 0:
        col = 2**N
    else:
        col = c
        
    rowBig = False
    colBig = False
    
    if row > 2 ** (N-1):
        rowBig = True
    if col > 2 ** (N-1):
        colBig = True
    
    if not rowBig and not colBig:
        add =0
    elif not rowBig and colBig:
        add = 1
    elif rowBig and not colBig:
        add = 2
    else:
        add = 3

    return add*2**(2*(N-1)) + getOrder(N-1,row % (2**(N-1)),col % (2**(N-1)))


N, r, c = map(int,input().split())

print(getOrder(N,r+1,c+1))
