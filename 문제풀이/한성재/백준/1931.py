#1931 회의실 배정

from collections import deque
import heapq
from sys import stdin


roomNumber = int(input())
performTimes = []


for _ in range(roomNumber):
    startTime, endTime = map(int, stdin.readline().rstrip().split())
    performTimes.append((startTime,endTime))

performTimes.sort()
performTimes.sort(key= lambda x: x[1])

performTimes = deque(performTimes)

sum = 0

end = performTimes.popleft()[1]
temp = []
sum += 1

for i in range(len(performTimes)):
    if performTimes[i][0] >= end:
        sum += 1
        end = performTimes[i][1]
    else:
        continue
print(sum)