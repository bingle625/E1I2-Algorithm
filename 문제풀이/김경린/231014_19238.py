# inf 알아가기
from collections import deque
import sys
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


n, m, fuel = map(int, input().split(' '))
board = []


# 벽 -1, 승객 번호 1-m, 
for _ in range(n):
    tmp = list(map(int, input().split(' ')))
    for i in range(n):
        if tmp[i] == 1:
            tmp[i] = -1

    board.append(tmp)


ty, tx = map(int, input().split(' '))
tx -= 1
ty -= 1
destination = [[] for _ in range(m+1)] # 승객 번호 [도착지 x, y]
for i in range(1, m+1):
    sy, sx, fy, fx = map(int, input().split(' '))
    sy -= 1
    sx -= 1
    fy -= 1
    fx -= 1
    board[sy][sx] = i
    destination[i] = [fx, fy]




def get_distance(sx, sy, fx, fy):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    deq = deque()
    deq.append((sx, sy, 0))
    visited[sy][sx] = 1

    while len(deq):
        x, y, dist = deq.popleft()
        if x==fx and y==fy:
            return dist
        for i in range(4):
            next_x = x+dx[i]
            next_y = y+dy[i]

            if 0<=next_x<n and 0<=next_y<n and board[next_y][next_x] != -1 and not visited[next_y][next_x]:
                deq.append((next_x, next_y, dist+1))
                visited[next_y][next_x] = 1    
    
    return sys.maxsize
            

def shortest_client(tx, ty):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    deq = deque()
    deq.append((tx, ty, 0))
    visited[ty][tx] = 1
    answer = []
    min_dist = sys.maxsize
    
    # 시작이 도착지라면
    if board[ty][tx] > 0:
        return tx, ty, 0

    while len(deq):
        x, y, dist = deq.popleft()

        for i in range(4):
            next_x = x+dx[i]
            next_y = y+dy[i]

            if 0<=next_x<n and 0<=next_y<n and board[next_y][next_x] != -1 and not visited[next_y][next_x]:
                if min_dist < dist + 1:
                    break
                if board[next_y][next_x] == 0:
                    deq.append((next_x, next_y, dist+1))
                    visited[next_y][next_x] = 1
                else:
                    min_dist = dist+1
                    answer.append([next_x, next_y, dist+1])
    
    answer.sort(key=lambda x: (x[1], x[0]))
    
    return [answer[0][0], answer[0][1], answer[0][2]] if len(answer) > 0 else [-1, -1, -1]


is_possible = True

for _ in range(m):
    # 가장 거리 짧은 승객 탐색
    target_x, target_y, dist = shortest_client(tx, ty)
    target_idx = board[target_y][target_x]

    # 데려다줄 수 있는 손님이 없는 경우
    if target_x == -1 and target_y == -1:
        is_possible = False
        break
    board[target_y][target_x] = 0
    fuel -= dist

    if fuel <= 0:
        is_possible = False
        break
    dist = get_distance(target_x, target_y, destination[target_idx][0], destination[target_idx][1] )
    fuel -= dist

    if fuel < 0:
        is_possible = False
        break
    fuel += 2*dist
    
    tx = destination[target_idx][0]
    ty = destination[target_idx][1]

if is_possible:
    print(fuel)
else:
    print(-1)



