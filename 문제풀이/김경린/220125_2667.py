
# def bfs(village, start_node):

#     queue = list()

#     queue.append(start_node)

#     while queue:
#         node = queue.pop(0)
#         if node not in visit:
#             visit.append(node)
#             queue.extend(village[node])

#     return visit


# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]

# size = int(input())
# village = {}

# arr = []
# for i in range(size):
#     arr.append(list(map(str, input().strip())))

# for height in range(size):
#     for width in range(size):
#         if arr[height][width] == '1':
#             neighbor = []
#             for i in range(4):
#                 if width+dx[i] >= 0 and width+dx[i] < size and height+dy[i] < size and height+dy[i] >= 0:
#                     if arr[height+dy[i]][width+dx[i]] == '1':
#                         neighbor.append(
#                             (height+dy[i])*size+width+dx[i])
#             village[size*height+width] = neighbor

# visit = []
# neighbor_nums = [0]
# cnt = 0
# for key in village:
#     if key not in visit:
#         bf_visit = len(visit)
#         neighbor_nums.append(len(bfs(village, key))-bf_visit)
#         cnt += 1

# neighbor_nums.sort()

# print(cnt)
# for num in neighbor_nums[1:]:
#     print(num)


from collections import deque


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


M = int(input())
village = [[0] for _ in range(M)]
visited = deque()

for i in range(M):
    tmp = input()
    village[i] = list(tmp)


def bfs(x,y):
    for k in range(4):
        next_x = x + dx[k]
        next_y = y + dy[k]
        if next_x>=0 and next_x<M and next_y>=0  and next_y<M and village[next_y][next_x]=='1':
            village[next_y][next_x] = 0
            visited.append([next_x,next_y])

village_cnt = []
for i in range(M):
    for j in range(M):
        if village[i][j]=='1':
            cnt = 0
            visited.append([j,i])
            village[i][j] = 0
            while visited:
                tmp = visited.popleft()
                point_x,point_y = tmp[0],tmp[1]
                bfs(point_x,point_y)
                cnt+=1

            village_cnt.append(cnt)

print(len(village_cnt))
village_cnt.sort()
for i in village_cnt:
    print(i)