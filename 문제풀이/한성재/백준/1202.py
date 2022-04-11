#파이썬 1202번

#시간 초과
# from collections import deque
# import heapq
# import sys


# N, K = map(int, input().split())
# jewels = []
# bag = []

# result = 0

# for _ in range(N):
#     weight, value = map(int,sys.stdin.readline().rstrip().split())
#     valuePerWeight = value / weight
#     jewels.append((weight,value))


# jewels.sort(key= lambda x: x[0])
# jewels.sort(key= lambda x: x[1], reverse= True)


# for _ in range(K):
#     heapq.heappush(bag,int(sys.stdin.readline().rstrip()))



# while bag:
#     container = heapq.heappop(bag)
    
#     for i in range(len(jewels)):
#         if container >= jewels[i][0]:
#             result += jewels[i][1]
#             jewels.pop(i)
#             break
#         else:
#             continue
            
# print(result)

import heapq
import sys


N, K =map(int, sys.stdin.readline().split())

jewelryList = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bagList = [int(sys.stdin.readline()) for _ in range(K)]
jewelryList.sort()
bagList.sort()

result = 0
temp = []

for bagWeight in bagList:
    while jewelryList and bagWeight >= jewelryList[0][0]:
        heapq.heappush(temp, -jewelryList[0][1])
        heapq.heappop(jewelryList)
    
    if temp:
        result += heapq.heappop(temp)
    elif not jewelryList:
        break

print(-result)