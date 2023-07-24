
# 회전
from sys import stdin


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

rect_dx = [1, 1, 0]
rect_dy = [0, 1, 1]

def isRect(x, y, target):
    for i in range(3):
        nx = x+rect_dx[i]
        ny = y+rect_dy[i]
        if (nx, ny) not in target:
            return False
    return True


def make_curve(stack, g):
    new_dragon = []
    x, y = stack[len(stack)-1]
    for i in range(len(stack)-1, 0, -1):
        d_x = stack[i][0] - stack[i-1][0]
        d_y = stack[i][1] - stack[i-1][1]

        if d_x == 1 and d_y == 0:
            nx, ny = x+dx[0], y+dy[0]
        elif d_x == 0 and d_y == -1:
            nx, ny = x+dx[1], y+dy[1]
        elif d_x ==  -1 and d_y == 0:
            nx, ny = x+dx[2], y+dy[2]
        else:
            nx, ny = x+dx[3], y+dy[3]

        new_dragon.append((nx, ny))
        x, y =nx, ny
    if g ==  0:
        return stack
    else:
        stack = make_curve(stack + new_dragon, g-1)
        return stack


        

n = int(stdin.readline().rstrip())
stacks = []

for i in range(n):
    stack = []
    x, y, d, g = map(int, stdin.readline().rstrip().split(' '))
    stack.append((x, y))
    if d == 0:
        stack.append((x+1, y))
    elif d == 1:
        stack.append((x, y-1))
    elif d == 2:
        stack.append((x-1, y))
    else:
        stack.append((x, y+1))
    
    stack = make_curve(stack, g)
    stacks.append(stack)

target = []
for i in range(n):
    target += stacks[i]
target = list(set(target))

cnt = 0

for x, y in target:
    if isRect(x, y, target):
        cnt += 1

print(cnt)