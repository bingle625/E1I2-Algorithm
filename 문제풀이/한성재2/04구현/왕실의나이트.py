

dx = [1,1,-1,-1,2,2,-2,-2]
dy = [2,-2,2,-2,1,-1,1,-1]

dic = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}

pos = list(input())

pos =  [dic[pos[0]],int(pos[1])]
cnt = 0

for i in range(8):
    if pos[0] + dx[i] < 1 or pos[0] +dx[i] > 8:
        continue
    if pos[1] + dy[i] < 1 or pos[1] +dy[i] > 8:
        continue
    cnt += 1

print(cnt)