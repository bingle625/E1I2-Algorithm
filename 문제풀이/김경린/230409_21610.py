dir_x = [-1, -1, 0, 1, 1, 1, 0, -1]
dir_y = [0, -1, -1, -1, 0, 1, 1, 1]

n, m = map(int, input().rstrip().split())

water = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    water[i] = list(map(int, input().rstrip().split()))

for i in range(m):
    over_water = []
    dir_idx, dist = map(int, input().rstrip().split())
    dir_idx -= 1
    if i == 0:
        cloud = [(0, n-1), (1, n-1), (0, n-2), (1, n-2)]
    for j in range(len(cloud)):
        x = cloud[j][0]
        y = cloud[j][1]
        cloud[j] = ((x +dir_x[dir_idx]*dist)%n, (y +dir_y[dir_idx]*dist)%n)
        water[cloud[j][1]][cloud[j][0]] += 1
    for x, y in cloud:
        cnt = 0
        for j in range(4):
            next_y = y + dir_y[2*j+1]
            next_x = x + dir_x[2*j+1]
            if 0 <= next_x < n and 0 <= next_y < n and water[next_y][next_x] > 0:
                cnt += 1
        water[y][x] += cnt
    
    for j in range(n):
        for k in range(n):
            if water[j][k] > 1:
                over_water.append((k,j))
    cloud = list(set(over_water) - set(cloud))
    for x, y in cloud:
        water[y][x] -= 2
    
water_sum = 0
for j in range(n):
    water_sum += sum(water[j])

print(water_sum)

    