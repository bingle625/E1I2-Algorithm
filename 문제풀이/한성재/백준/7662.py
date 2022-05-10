#7662번 이중 우선순위 큐

from collections import deque
import heapq
from sys import stdin
import sys


T = int(input())

def mul(n):
    n *= -1
    return n

for _ in range(T):
    numbers = int(input())
    arrMax = []
    arrMin = []
    status = [False] * numbers
    
    for i in range(numbers):
        command, number = stdin.readline().rstrip().split()
        
        number = int(number)
        if command == 'I':
            status[i] = True
            heapq.heappush(arrMax,(-number,i))
            heapq.heappush(arrMin,(number,i))
            
        else:
            if number == 1:
                while arrMax and not status[arrMax[0][1]]:
                    heapq.heappop(arrMax)
                if arrMax:
                    status[arrMax[0][1]] = False
                    heapq.heappop(arrMax)
            else:
                while arrMin and not status[arrMin[0][1]]:
                    heapq.heappop(arrMin)
                if arrMin:
                    status[arrMin[0][1]] = False
                    heapq.heappop(arrMin)
                    
    empty = True
    while arrMax and not status[arrMax[0][1]]:
        heapq.heappop(arrMax)
    while arrMin and not status[arrMin[0][1]]:
        heapq.heappop(arrMin)

    if not arrMax or not arrMin:
        print("EMPTY")
    else:
        print(-heapq.heappop(arrMax)[0], heapq.heappop(arrMin)[0])
