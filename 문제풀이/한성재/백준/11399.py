# 11399번 ATM

import heapq
from sys import stdin


number = int(input())

arr = list(map(int, stdin.readline().rstrip().split()))

timeSum = 0

heapq.heapify(arr)
for i in range(number):
    timeSum += (number - i) * heapq.heappop(arr)

print(timeSum)
