# 예제 4-1

N = int(input())
moves = list(input().split())

x, y = 1, 1
for move in moves:
    if move == 'R' and x < N:
        x += 1
    elif move == 'L' and x > 1:
        x -= 1
    elif move == 'U' and y < 1:
        y -= 1
    elif move == 'D' and y < N:
        y += 1

print(y, x)