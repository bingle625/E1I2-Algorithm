
import heapq
from sys import stdin

N = int(stdin.readline().rstrip())
li = []
for _ in range(N):
    number = int(stdin.readline().rstrip())
    if number == 0:
        if len(li) == 0:
            print(0)
        else:
            print(heapq.heappop(li))
    else:
            heapq.heappush(li,number)