
def bfs(village, start_node):

    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(village[node])

    return visit


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

size = int(input())
village = {}

arr = []
for i in range(size):
    arr.append(list(map(str, input().strip())))

for height in range(size):
    for width in range(size):
        if arr[height][width] == '1':
            neighbor = []
            for i in range(4):
                if width+dx[i] >= 0 and width+dx[i] < size and height+dy[i] < size and height+dy[i] >= 0:
                    if arr[height+dy[i]][width+dx[i]] == '1':
                        neighbor.append(
                            (height+dy[i])*size+width+dx[i])
            village[size*height+width] = neighbor

visit = []
neighbor_nums = [0]
cnt = 0
for key in village:
    if key not in visit:
        bf_visit = len(visit)
        neighbor_nums.append(len(bfs(village, key))-bf_visit)
        cnt += 1

neighbor_nums.sort()

print(cnt)
for num in neighbor_nums[1:]:
    print(num)
