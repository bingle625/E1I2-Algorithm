from collections import deque, defaultdict

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, k = map(int, input().split(' '))
board = []

for i in range(n):
	tmp = input().split(' ')
	board.append(tmp)
	
village_dict = defaultdict(int)

def bfs():
	visited = [[0 for _ in range(n)] for _ in range(n)]
	for y in range(n):
		for x in range(n):
			if visited[y][x] == 0:
				type_num = board[y][x]
				tmp = deque()
				tmp.append((x, y))
				visited[y][x] = 1
				cnt = 1
				while len(tmp):
					cx, cy = tmp.popleft()
					for i in range(4):
						nx = cx + dx[i]
						ny = cy + dy[i]
						if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and board[ny][nx] == type_num:
							visited[ny][nx] = 1
							tmp.append((nx, ny))
							cnt += 1
				if cnt >= k:
					village_dict[type_num] += 1
	max_key = '0'
	max_val = 0
	for key in village_dict.keys():
		if village_dict[key] >= max_val:
			if village_dict[key] == max_val:
				max_key = max(key, max_key)
			else:
				max_key = key
			max_val = village_dict[key]
	return max_key

answer = bfs()
print(answer)
		
					
			