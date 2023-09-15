from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


	
n = int(input())
board = []

for i in range(n):
	tmp = list(map(int, input().split(' ')))
	board.append(tmp)

# visited = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
for i in range(n):
	for j in range(n):
		if board[i][j] == 1:
			cnt += 1
			elect = deque()
			elect.append((j,i))
			board[i][j] = 0
			while len(elect):
				x, y = elect.popleft()
				for d in range(4):
					next_x = x + dx[d]
					next_y = y + dy[d]
					if 0<=next_x<n and 0<=next_y<n:
						if board[next_y][next_x] == 1:
							elect.append((next_x, next_y))
							board[next_y][next_x] = 0
print(cnt)


	
