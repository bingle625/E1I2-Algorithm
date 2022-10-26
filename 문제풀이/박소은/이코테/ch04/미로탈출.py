from collections import deque

graph = []
N, M = map(int, input())    # N: 세로길이, M: 가로길이
for _ in range(N):
    graph.append(list(map(int, input())))

moves = [[0, -1], [0, 1], [-1, 0], [1, 0]] # 상, 하, 좌, 우
answer = 0

def bfs(graph, startx, starty):
    queue = deque([(0, 0)])
    graph[0][0] = 0

    while queue:
        currentX, currentY = queue.popleft()
        for moveX, moveY in moves:
            X = currentX + moveX
            Y = currentY + moveY
            if 0 <= X < M and 0 <= Y < N and graph[X][Y] == 0:
                queue.append((X, Y))
    answer += 1

print(bfs(graph, 0, 0))
