N = int(input())
K = int(input())

apples = []
directions = [(1,0),(0,1),(-1,0),(0,-1)]
dic = {}
head = [1,1]
body = [(1,1)]

for i in range(K):
    y, x = map(int,input().split())
    apples.append((x,y))

L = int(input())

for i in range(L):
    time, direction = input().split()
    dic[int(time)] = direction
    
time = 0
cur_di = 0

while True:
    time += 1
    
    head[0] += directions[cur_di][0]
    head[1] += directions[cur_di][1]
    
    # 이동 후 종료인지,
    # 종료가 아니라면, 사과인지 아닌지 파악
    if head[0] > N or head[0] < 1:
        break
    
    if head[1] > N or head[1] < 1:
        break
    
    if (head[0], head[1]) in body:
        break
    
    #사과인지 파악
    if (head[0], head[1]) in apples:
        apples.remove((head[0],head[1]))
        body.append((head[0],head[1]))
    else:
        body.pop(0)
        body.append((head[0],head[1]))
    
    # 방향은 마지막에 바뀜
    if time in dic:
        if dic[time] == "D":
            cur_di += 1
        else:
            cur_di -= 1
        cur_di %= 4
        
print(time)