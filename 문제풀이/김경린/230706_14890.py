from collections import deque


n, l = map(int, input().split(' '))


def check_crossing(road, l):
    tmp = []
    road = deque(road)
    tmp.append(road.popleft())
    while len(road):
        last_road = tmp[-1] if len(tmp) else point
        point = road.popleft()
        if last_road == point:
            tmp.append(point)
        elif last_road == point + 1: # 내리막길
            for j in range(l-1):
                if len(road):
                    next = road.popleft()
                    if next != point:
                        return False
                else:
                    return False
            tmp = []
        elif last_road == point - 1: # 오르막길
            for j in range(l):
                if len(tmp):
                    if tmp[-1] != last_road:
                        return False
                    else:
                        tmp.pop()
                else:
                    return False
            tmp = [point]
        else:
            return False
    return True
            



maps = []
cross_roads = 0
for i in range(n):
    tmp = list(map(int, input().split(' ')))
    maps.append(tmp)
    if check_crossing(tmp, l):
        # print('---', tmp)
        cross_roads += 1

for i in range(n):
    col = []
    for j in range(n):
        col.append(maps[j][i])
    
    if check_crossing(col, l):
        # print('---',col)
        cross_roads += 1

print(cross_roads)


