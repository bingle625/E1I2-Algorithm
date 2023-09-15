from collections import deque

n, k, q = map(int, input().split(' '))
board=[]

dx = [1, 0 , -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
	tmp = list(input())
	board.append(tmp)
	
def print_board():
	for b in board:
		print(''.join(b))

def bfs():
	visited = [[0 for _ in range(n)] for _ in range(n)]
	cnt = 0
	for i in range(n):
		for j in range(n):
			if not visited[i][j] and board[i][j] != '.':
				# print((j,i))
				visited[i][j] = 1
				deq = deque()
				components = []
				deq.append((j,i))
				components.append((j,i))
				val = board[i][j]
				while len(deq):
					x, y = deq.popleft()
					for nd in range(4):
						ny = y + dy[nd]
						nx = x + dx[nd]
						if 0<=nx<n and 0<=ny<n and not visited[ny][nx] and board[ny][nx] == val:
							deq.append((nx, ny))
							components.append((nx, ny))
							visited[ny][nx] = 1
				if len(components) >= k:
					for x, y in components:
						board[y][x] = '.' 
				
for i in range(q):
	tmp = input().split(' ')
	y, x, d = int(tmp[0])-1, int(tmp[1])-1, tmp[2]
	board[y][x] = d
	bfs()
print_board()
