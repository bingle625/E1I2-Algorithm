# board[][] = []
# 1 수평방향 -1 수직방향

n, m = map(int, input().split(' '))
board = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
	y, x, d = input().split(' ')
	x, y = int(x)-1, int(y)-1
	if d=='U':
		for i in range(y+1):
			board[i][x].append(-1)
	elif d=='D':
		for i in range(y, n):
			board[i][x].append(-1)
	elif d=='L':
		for i in range(x+1):
			board[y][i].append(1)
	elif d=='R':
		for i in range(x, n):
			board[y][i].append(1)

cnt = 0
for i in range(n):
	for j in range(n):
		cnt += board[i][j].count(1) * board[i][j].count(-1)
print(cnt)
		