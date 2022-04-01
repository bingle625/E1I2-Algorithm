
#가방은 무게가 작은거 부터
#보석을 비싼 거 부터
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
    heapq.heappush(jewels,(-price,weight))

for i in range(bag_num):
    bag = int(stdin.readline().strip())
    bags.append(bag)

bags = sorted(bags)

sum =0

def get_jewel(jewels,bag):
    while len(jewels):
        jewel = heapq.heappop(jewels)
        if jewel[1]<=bag:
            return jewel[0]
        else:
            val = get_jewel(jewels,bag)
            heapq.heappush(jewels,(jewel[0],jewel[1]))
            return val
    # 담을 수 있는 보석이 없을 때
    return 0

for bag in bags:
    sum -= get_jewel(jewels,bag)

print(sum)