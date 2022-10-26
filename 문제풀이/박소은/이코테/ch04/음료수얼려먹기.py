# 실패

from collections import deque

graph = []
N, M = map(int, input().split())    # N: 세로 길이, M: 가로 길이
for _ in range(N):
    graph.append(list(map(int, list(input()))))

def isFinished(graph):
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return (i, j)
    return True

def printGraph(graph):
    for i in range(N):
        print(graph[i])
    print()

def bfs(graph, startx, starty):
    answer = 0
    queue = deque([])
    moves = [[0, -1], [0, 1], [-1, 0], [1, 0]] # 상, 하, 좌, 우
    
    while True:
        printGraph(graph)
        finish = isFinished(graph)
        if finish == True:
            return answer
        else:
            queue.append((finish[0], finish[1]))
            graph[finish[0]][finish[1]] = 1

        while queue:
            currentX, currentY = queue.popleft()
            for moveX, moveY in moves:  # 상하좌우로 움직이기
                X = currentX + moveX
                Y = currentY + moveY
                if 0 <= X < M and 0 <= Y < N and graph[X][Y] == 0:
                    queue.append((X, Y))
        answer += 1

print(bfs(graph, 0, 0))