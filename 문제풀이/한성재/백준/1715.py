# 1715번 카드 정렬하기
import heapq


num = int(input())
numList = []
sum = 0

for _ in range(num):
    numList.append(int(input()))

q = heapq.heapify(numList)

for _ in range(num-1):
    elem1 = heapq.heappop(numList)
    elem2 = heapq.heappop(numList)
    sum+=elem1+elem2
    heapq.heappush(numList,elem1+elem2)
    
print(sum)