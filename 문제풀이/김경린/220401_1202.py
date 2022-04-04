
#가방은 무게가 작은거 부터
#보석은 가벼운거부터 넣고 그 중 가치가 높은 것을 선택
#dict = {가격:무게}

from collections import defaultdict, deque
import heapq
import sys
sys.setrecursionlimit(10**6)

from sys import stdin

jewel_num, bag_num = map(int,stdin.readline().split())

jewels = []

bags = []

for i in range(jewel_num):
    weight, price = map(int,stdin.readline().split())
    heapq.heappush(jewels,(weight,price))

for i in range(bag_num):
    bag = int(stdin.readline().strip())
    bags.append(bag)

bags = sorted(bags)

sum =0

availJewel = []

for bag in bags:
    
    while len(jewels) and bag>=jewels[0][0]:
        jewel = heapq.heappop(jewels)
        heapq.heappush(availJewel,-jewel[1])
    
    if len(availJewel):
        sum -= heapq.heappop(availJewel)
    if not len(jewels):
        break


    

print(sum)