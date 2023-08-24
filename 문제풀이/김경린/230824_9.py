dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, k = map(int, input().split(' '))

board = []
for _ in range(n):
	tmp = input().split(' ')
	board.append(tmp)

bomb = [[0 for _ in range(n)] for _ in range(n)]

def increase_bomb(x, y):
	global bomb
	if board[y][x] == '#':
		return
	elif board[y][x] == '@':
		bomb[y][x] += 2
	else:
		bomb[y][x] += 1


for i in range(k):
	y, x = map(int, input().split(' '))
	x -= 1
	y -= 1
	increase_bomb(x, y)
	for j in range(4):
		next_x = x + dx[j]
		next_y = y + dy[j]
		if 0<=next_x<n and 0<=next_y<n:
			increase_bomb(next_x, next_y)

answer = 0
for i in range(n):
	answer = max(answer, max(bomb[i]))
print(answer)		
	