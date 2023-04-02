from collections import deque

### 2023.04.02 풀이

def bfs() -> int:
    queue = deque([(0, 0)])
    
    while queue:
        v = queue.popleft() # 큐에서 원소 꺼내기
        
        dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            nx, ny = v[0]+dx[i], v[1]+dy[i]
            if 0 <= nx < n and 0 <= ny < m: # grid 범위 안에 있을 때
                if grid[nx][ny] == 1:  # 이동할 수 있는 칸일 때
                    grid[nx][ny] = grid[v[0]][v[1]] + 1
                    queue.append((nx, ny))

    return grid[n-1][m-1]


n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input())))

print(bfs())




### 2022년 풀이(실패)

# # BFS 활용한 풀이 1
# # 실패 (최단거리를 못 찾음)
# def maze(graph: List[List[int]]) -> int:
#     def bfs():
#         queue = [[0,0]]
#         n, m, count = 0, 0, 1
#         while queue and n < len(graph) and m < len(graph):
#             v = queue.pop(0)
#             # 상
#             if v[0] + 1 < len(graph) and graph[v[0]+1][v[1]] == 1:
#                 queue.append([v[0]+1, v[1]])
#                 n += 1
#                 count += 1
#             # 하
#             if v[0] - 1 > 0 and graph[v[0]-1][v[1]] == 1:
#                 queue.append([v[0]-1, v[1]])
#                 n -= 1
#                 count += 1
#             # 우
#             if v[1] + 1 < len(graph[0]) and graph[v[0]][v[1]+1] == 1:
#                 queue.append([v[0], v[1]+1])
#                 m += 1
#                 count += 1
#             # 좌
#             if v[1] - 1 > 0 and graph[v[0]][v[1]-1] == 1:
#                 queue.append([v[0], v[1]-1])
#                 m -= 1
#                 count += 1

#         return count
    
#     return bfs()

# # BFS 활용한 풀이 2
# # 런타임 에러
# def bfs(graph: List[List[int]]):
#     queue = [[0, 0]]
#     count = 0
#     while queue:
#         v = queue.pop(0)
#         count = graph[v[0]][v[1]]   # 최단거리

#         # 미로를 탈출했을 때
#         if v[0] == len(graph)-1 and v[1] == len(graph[0])-1:
#             return count

#         # 하
#         if v[0]+1 < len(graph) and graph[v[0]+1][v[1]] == 1:
#             graph[v[0]+1][v[1]] = graph[v[0]][v[1]] + 1
#             queue.append([v[0]+1, v[1]])
#         # 우
#         if v[1]+1 < len(graph[0]) and graph[v[0]][v[1]+1] == 1:
#             graph[v[0]][v[1]+1] = graph[v[0]][v[1]] + 1
#             queue.append([v[0], v[1]+1])
#         # 상
#         if v[0]-1 >= 0 and graph[v[0]-1][v[1]] == 1:
#             graph[v[0]-1][v[1]] = graph[v[0]][v[1]] + 1
#             queue.append([v[0]-1, v[1]])
#         # 좌
#         if v[1]-1 >= 0 and graph[v[0]][v[1]-1] == 1:
#             graph[v[0]][v[1]-1] = graph[v[0]][v[1]] + 1
#             queue.append([v[0], v[1]-1])


# # 입력
# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))

# print(bfs(graph))


# # BFS 활용한 풀이 2.1 - 최적화
# # 런타임 에러
# def bfs(graph: List[List[int]], n: int, m: int):
#     # n: len(graph), m: len(graph[0])
#     count = 1
#     queue = [[0, 0]]
#     while queue:
#         x, y = queue.pop(0)

#         # 미로를 탈출했을 때
#         if x == n-1 and y == m-1:
#             count = graph[x][y]
#             break

#         # 하
#         if x+1 < n and graph[x+1][y] == 1:
#             graph[x+1][y] = graph[x][y] + 1
#             queue.append([x+1, y])
#         # 우
#         if y+1 < m and graph[x][y+1] == 1:
#             graph[x][y+1] = graph[x][y] + 1
#             queue.append([x, y+1])
#         # 상
#         if x-1 >= 0 and graph[x-1][y] == 1:
#             graph[x-1][y] = graph[x][y] + 1
#             queue.append([x-1, y])
#         # 좌
#         if y-1 >= 0 and graph[x][y-1] == 1:
#             graph[x][y-1] = graph[x][y] + 1
#             queue.append([x, y-1])
#     return count


# # 입력
# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))

# print(bfs(graph, n, m))
