# 나무를 저장할 때 dictionary에 저장하면 시간 초과 
# 좌표 2차원 배열에 deque를 저장하기 -> 매번 dict.keys로 찾는 것보다 for i in range(n) 으로 이중 for문 도는 것이 더 효율적
from collections import defaultdict, deque
from sys import stdin

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, stdin.readline().rstrip().split(' '))

new_nutrients = []
nutrients = [[5 for _ in range(n)] for _ in range(n)]

for i in range(n):
    tmp = list(map(int, stdin.readline().rstrip().split(' ')))
    new_nutrients.append(tmp)

trees = [[deque() for _ in range(n)] for _ in range(n)]

for i in range(m):
    y, x, age = map(int, stdin.readline().rstrip().split(' '))
    y -= 1
    x -= 1
    tmp = []
    for j in range(len(trees[y][x])):
        if trees[y][x][j] < age:
            break
        else: 
            tmp.append(trees[y][x].pop())
    trees[y][x].append(age)
    while len(tmp):
        trees[y][x].append(tmp.pop())


for i in range(k):
    fall_breeding = []
    # 봄
    for y in range(n):
        for x in range(n):
            for idx in range(len(trees[y][x])):
                if nutrients[y][x] >= trees[y][x][idx]:
                    nutrients[y][x] -= trees[y][x][idx]
                    trees[y][x][idx] += 1
                    if trees[y][x][idx] % 5 == 0:
                        fall_breeding.append((x,y))
                else:
                    # 여름
                    for idx in range(idx, len(trees[y][x])):
                        nutrients[y][x] += trees[y][x].pop() // 2
                    break
        
    for x,y in fall_breeding:
        # 가을
        for dir in range(8):
            next_x = x+dx[dir]
            next_y = y+dy[dir]
            if 0<=next_x<n and 0<=next_y<n:
                trees[next_y][next_x].appendleft(1)
    # 겨울    
    for y in range(n):
        for x in range(n):
            nutrients[y][x] += new_nutrients[y][x]

alive_num = 0
for y in range(n):
    for x in range(n):
        alive_num += len(trees[y][x])


print(alive_num)

             

            
        
    
