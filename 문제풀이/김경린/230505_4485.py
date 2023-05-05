# from sys import stdin
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# def get_min_node():
#     min_dist = float('inf')
#     for i in range(n):
#         for j in range(n):
#             if distance[i][j] < min_dist and not visited[i][j]:
#                 min_dist = distance[i][j]
#                 min_x, min_y = j, i
#     return min_x, min_y

# def dijkstra():
#     x, y = start
#     distance[y][x] = cave[y][x]
#     visited[y][x] = 1

#     for i in range(4):
#         next_x = x + dx[i]
#         next_y = y + dy[i]
#         if 0 <= next_x < n and 0 <= next_y <n:
#             distance[next_y][next_x] = distance[y][x] + cave[next_y][next_x]
    
#     for y in range(n):
#         for x in range(n):
#             if x == 0 and y == 0:
#                 continue
#             min_x, min_y = get_min_node()
#             visited[min_y][min_x] = 1
#             for i in range(4):
#                 next_x = min_x + dx[i]
#                 next_y = min_y + dy[i]
#                 if 0 <= next_x < n and 0 <= next_y <n:
#                     new_dist = distance[min_y][min_x] + cave[next_y][next_x]
#                     distance[next_y][next_x] = min(new_dist, distance[next_y][next_x])



# idx = 1
# while True:
#     n = int(stdin.readline().rstrip())
#     if n == 0:
#         break
#     cave = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         cave[i] = list(map(int, stdin.readline().rstrip().split()))
#     start = (0,0)
#     visited = [[ 0 for _ in range(n)] for _ in range(n)]
#     distance = [[ float('inf')-1 for _ in range(n)] for _ in range(n)]
#     dijkstra()
#     print("Problem",idx,":",distance[n-1][n-1])
#     idx += 1
    



from sys import stdin
import heapq
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dijkstra():
    x, y = start
    distance[y][x] = cave[y][x]
    q = []
    heapq.heappush(q, (distance[y][x],(x,y)))

    while len(q):
            min_dist, min_pos = heapq.heappop(q)
            min_x, min_y = min_pos
            if min_dist > distance[min_y][min_x]:
                continue

            for i in range(4):
                next_x = min_x + dx[i]
                next_y = min_y + dy[i]
                if 0 <= next_x < n and 0 <= next_y <n:
                    new_dist = min_dist + cave[next_y][next_x]
                    if new_dist < distance[next_y][next_x]:
                        distance[next_y][next_x] = min(new_dist, distance[next_y][next_x])
                        heapq.heappush(q, (new_dist, (next_x, next_y)))



idx = 1
while True:
    n = int(stdin.readline().rstrip())
    if n == 0:
        break
    cave = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        cave[i] = list(map(int, stdin.readline().rstrip().split()))
    start = (0,0)
    distance = [[ float('inf')-1 for _ in range(n)] for _ in range(n)]
    dijkstra()
    answer ="Problem {0}: {1}".format(idx, distance[n-1][n-1])
    print(answer)
    idx += 1
    



# 백준 4485 다익스트라 for문(시간초과), heapq
# 프로그래머스 72413 합승 택시 적용해보기