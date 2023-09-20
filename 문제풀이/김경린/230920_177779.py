
from sys import maxsize

n = int(input())
board = []
for i in range(n):
    tmp = list(map(int, input().split(' ')))
    board.append(tmp)

def calculate(x, y, d1, d2):
    # 1번 구역
    population1 = 0
    col = y
    for i in range(x+d1-1):
        if i >= x-1:
            col -= 1
        population1 += sum(board[i][:col])
        
    # 2번 구역
    population2 = 0
    col = y
    for i in range(x+d2):
        if i >= x:
            col += 1
        population2 += sum(board[i][col:])

    # 3번 구역
    population3 = 0
    col = y-d1-2
    for i in range(x+d1-1, n):
        if i < x+d1+d2:
            col += 1
        population3 += sum(board[i][:col])

    # 4 번 구역
    population4 = 0
    col = y+d2
    for i in range(x+d2, n):
        if i <= x+d1+d2:
            col -= 1
        population4 += sum(board[i][col:])
    
    

    total_sum = 0
    for x in board:
        total_sum += sum(x)

    population5 = total_sum - (population1+population2+population3+population4)

    populations = [population1, population2, population3, population4, population5]
    # print(populations)
    return max(populations) - min(populations)

min_diff = maxsize

for y in range(n):
    for x in range(n):
        for d1 in range(1, n-2):
            for d2 in range(1, n-2):
                if y+d2<=n and x+d1+d2<=n and 0<=y-d1-1:
                    min_diff = min(min_diff, calculate(x, y, d1, d2))

print(min_diff)