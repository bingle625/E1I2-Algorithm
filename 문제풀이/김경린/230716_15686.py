from collections import deque
from copy import deepcopy
import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# def bfs(town, start_x, start_y):
#     # print(town)
#     n = len(town)
#     dist = 0
#     deq = deque()
#     deq.append([(start_x, start_y), dist])
#     visited = [[0 for _ in range(n)] for _ in range(n)]
#     visited[start_y][start_x] = 1

#     while len(deq):
#         tmp = deq.popleft()
#         v = tmp[0]
#         dist = tmp[1] 
#         for i in range(4):
#             next_x = v[0] + dx[i]
#             next_y = v[1] + dy[i]
#             if 0<=next_x<n and 0<= next_y <n and not visited[next_y][next_x]:
#                 visited[next_y][next_x] = 1
#                 if town[next_y][next_x] == '2':
#                     return dist+1
#                 else:
#                     deq.append([(next_x, next_y), dist+1])

def get_dist(x, y, picked):
    min_d = sys.maxsize
    for i in range(len(picked)):
        d = abs(picked[i][0]-x) + abs(picked[i][1]-y)
        min_d = min(min_d, d)

    return min_d

min_dist = sys.maxsize

def pick_chicken(town, idx, cnt, picked):
    global min_dist
    if cnt == m:
        dists = 0
        for i in range(len(house)):
            dists += get_dist(house[i][0], house[i][1], picked)
        min_dist = min(dists, min_dist)
        return
            
    else:
        for i in range(idx, len(chicken)):
            picked.append(chicken[i])
            pick_chicken(town, i+1, cnt+1, picked)
            picked.pop()
        
        

n, m = map(int, sys.stdin.readline().rstrip().split(' '))

town = []
house = []
chicken = []
for i in range(n):
    tmp = sys.stdin.readline().rstrip().split(' ')
    town.append(tmp)
    for j in range(n):
        if tmp[j] == '1':
            house.append((j,i))
        elif tmp[j] == '2':
            chicken.append((j,i))
pick_chicken(town, 0, 0,[])
print(min_dist)




    



