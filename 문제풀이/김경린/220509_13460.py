from collections import deque
from sys import stdin

dx = [1,0,-1,0]
dy = [0,-1,0,1]

length, width = map(int,stdin.readline().split())
board = [ 0 for _ in range(length)]
visited = [[[[0 for _ in range(length)] for _ in range(width)] for _ in range(length)] for _ in range(width)]    #visited[bx][by][rx][ry]

for i in range(length):
    board[i] = list(stdin.readline().rstrip())
    if 'B' in board[i]:
        stateB = deque()
        stateB.append([board[i].index('B'), i])
    if 'R' in board[i]:
        stateR = deque()
        stateR.append([[board[i].index('R'), i],0])
    if 'O' in board[i]:
        stateO = [board[i].index('O'), i]


visited[stateB[0][0]][stateB[0][1]][stateR[0][0][0]][stateR[0][0][1]] = 1

# 0은 그냥 실패 1은 성공 -1을 앞으로 불가능
# 둘이 좌표가 같을 때 구멍에 빠졌을 때]
# stateB R 복사

def move(x,y,dx,dy):
    m = 0
    
    while board[y][x] != 'O' and board[y+dy][x+dx] != '#':
        x += dx
        y += dy
        m += 1
    return x,y,m

    
    


def bfs():
    cnt = 0
    while True:
        b = stateB.popleft()
        tmp = stateR.popleft() 
        r, cnt = tmp[0], tmp[1] 
        if cnt > 10:
            print(-1)
            return 0
        for i in range(4):
            
            bx,by,bm = move(b[0],b[1],dx[i],dy[i])
            rx,ry,rm = move(r[0],r[1],dx[i],dy[i])

            if board[by][bx] != 'O':
                if board[ry][rx]=='O':
                    print(cnt+1)
                    return 0
            
                if bx==rx and by==ry:
                    if bm > rm:
                        bx -= dx[i]
                        by -= dy[i]
                    else:
                        rx -= dx[i]
                        ry -= dy[i]
        
                if visited[bx][by][rx][ry]==0:
                    visited[bx][by][rx][ry]=1
                    stateB.append([bx,by])
                    stateR.append([[rx,ry],cnt + 1])

            else:
                print(-1)
                return 0
                

        


            
            
bfs()



            


