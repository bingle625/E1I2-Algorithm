import heapq
import sys


N, K = map(int, input().split())
jewels = []
bag = []
result = 0

for _ in range(N):
    weight, value = map(int,sys.stdin.readline().rstrip().split())
    valuePerWeight = value / weight
    jewels.append((valuePerWeight,weight,value))

jewels.sort(key= lambda x:x[0], reverse= True)

for _ in range(K):
    heapq.heappush(bag,int(sys.stdin.readline().rstrip()))


while bag:
    container = heapq.heappop(bag)
    for item in jewels:
        if item[1] <= container:
            result += item[2]
            jewels.remove(item)
            break
        else:
            continue
print(result)