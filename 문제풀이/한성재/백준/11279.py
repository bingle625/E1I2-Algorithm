# 11279번 최대 힙

import heapq
from sys import stdin


r = int(input())
arr = []

for i in range(r):
    number = int(stdin.readline().rstrip())
    if number == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -number)
