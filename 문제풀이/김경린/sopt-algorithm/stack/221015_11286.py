import heapq
from sys import stdin
num = int(stdin.readline())
heap = []
for i in range(num):
    instruction = int(stdin.readline())
    if instruction == 0:
        if len(heap):
            min_num = heapq.heappop(heap)
            print(min_num[1])
        else:
            print(0)
    else:
        if instruction < 0:
            heapq.heappush(heap, (-instruction, instruction))
        else:
            heapq.heappush(heap, (instruction, instruction))
        
