n = int(input())
goorm_p = list(map(int, input().split(' ')))
player_p = list(map(int, input().split(' ')))

board = []
for _ in range(n):
	tmp = list(input().split(' '))
	board.append(tmp)


def play(player):
	visited = [[0 for _ in range(n)] for _ in range(n)]
	cnt = 1
	y, x = player[0]-1, player[1]-1
	visited[y][x] = 1
	while True:
		
		count, direction = board[y][x][:-1], board[y][x][-1]
		count = int(count)
		
		if direction == 'U':
			while count > 0:
				visited[y][x] = 1
				count -= 1
				y -= 1
				if y < 0:
					y = n-1
				if visited[y][x] == 1:
					return cnt
				cnt += 1
				
		elif direction == 'D':
			while count > 0:
				visited[y][x] = 1
				count -= 1
				y += 1
				if y >= n:
					y = 0
				if visited[y][x] == 1:
					return cnt
				cnt += 1
				
		elif direction == 'R':
			while count > 0:
				visited[y][x] = 1
				count -= 1
				x += 1
				if x >= n:
					x = 0
				if visited[y][x] == 1:
					return cnt
				cnt += 1
				
		elif direction == 'L':
			while count > 0:
				visited[y][x] = 1
				count -= 1
				x -= 1
				if x < 0:
					x = n-1
				if visited[y][x] == 1:
					return cnt
				cnt += 1
	
	return cnt

goorm_score = play(goorm_p)
player_score = play(player_p)
if goorm_score > player_score:
	print('goorm',end=' ')
	print(goorm_score)
	# print(player_score)
else:
	print('player', end=' ')
	# print(goorm_score)
	print(player_score)
			
	