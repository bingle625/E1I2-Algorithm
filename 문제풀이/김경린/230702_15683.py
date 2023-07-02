from collections import defaultdict, deque
from copy import deepcopy

dxy = [[1,0], [0, 1], [-1,0], [0,-1]]

n, m = map(int, input().split(' '))
maps = []
cctvs = deque()
for i in range(n):
    tmp = list(map(int, input().split(' ')))
    maps.append(tmp)
    for x in range(len(tmp)):
        if 0<tmp[x]<6:
            cctvs.append([x,i])

visited = []
min_hidden = n*m

def get_zeros(maps):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                cnt += 1
    return cnt

def visit(maps, x, y, i):
    while 0 <= x < m and 0 <= y < n and maps[y][x] != 6:
        if maps[y][x] == 0:
            maps[y][x] = 7
        x += dxy[i][0]
        y += dxy[i][1]

    return maps 

def get_hidden(cctv_idx, maps):
    global cctvs, min_hidden

    if cctv_idx == len(cctvs):
        tmp = get_zeros(maps)
        min_hidden = min(min_hidden, tmp)
        return min_hidden

    xy = cctvs[cctv_idx]
    x = xy[0]
    y = xy[1]
    cctv_num = maps[y][x]

    if cctv_num == 1:
        for i in range(4):
            new_maps = deepcopy(maps)
            new_x = x+dxy[i][0]
            new_y = y+dxy[i][1]
            new_maps = visit(deepcopy(maps), new_x, new_y, i)

            get_hidden(cctv_idx+1, new_maps)
    elif cctv_num == 2:
        for i in range(2):
            new_x = x+dxy[i][0]
            new_y = y+dxy[i][1]
            new_maps = visit(deepcopy(maps), new_x, new_y, i)
            
            new_x = x+dxy[i+2][0]
            new_y = y+dxy[i+2][1]
            new_maps = visit(new_maps, new_x, new_y, i+2)
            
            get_hidden(cctv_idx+1, new_maps)
    elif cctv_num == 3:
        for i in range(4):
            new_maps = deepcopy(maps)
            new_x = x+dxy[i][0]
            new_y = y+dxy[i][1]
            new_maps = visit(deepcopy(maps), new_x, new_y, i)
    
            
            new_x = x+dxy[(i+1)%4][0]
            new_y = y+dxy[(i+1)%4][1]
            new_maps = visit(new_maps, new_x, new_y, (i+1)%4)

            get_hidden(cctv_idx+1, new_maps)
    elif cctv_num == 4:
        for i in range(4):
            new_maps = deepcopy(maps)
            new_x = x+dxy[i][0]
            new_y = y+dxy[i][1]
            new_maps = visit(deepcopy(maps), new_x, new_y, i)
            
            new_x = x+dxy[(i+1)%4][0]
            new_y = y+dxy[(i+1)%4][1]
            new_maps = visit(new_maps, new_x, new_y, (i+1)%4)

            new_x = x+dxy[(i+2)%4][0]
            new_y = y+dxy[(i+2)%4][1]
            new_maps = visit(new_maps, new_x, new_y, (i+2)%4)
            
            get_hidden(cctv_idx+1, new_maps)

    elif cctv_num == 5:
        i = 0
        new_maps = deepcopy(maps)
        new_x = x+dxy[i][0]
        new_y = y+dxy[i][1]
        new_maps = visit(deepcopy(maps), new_x, new_y, i)
        
        new_x = x+dxy[(i+1)%4][0]
        new_y = y+dxy[(i+1)%4][1]
        new_maps = visit(new_maps, new_x, new_y, (i+1)%4)

        new_x = x+dxy[(i+2)%4][0]
        new_y = y+dxy[(i+2)%4][1]
        new_maps = visit(new_maps, new_x, new_y, (i+2)%4)
        
        new_x = x+dxy[(i+3)%4][0]
        new_y = y+dxy[(i+3)%4][1]
        new_maps = visit(new_maps, new_x, new_y, (i+3)%4)
        
        get_hidden(cctv_idx+1, new_maps)

get_hidden(0, maps)

print(min_hidden)