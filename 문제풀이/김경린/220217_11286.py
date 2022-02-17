import heapq
import sys

input_data = []

heap = []

num = int(sys.stdin.readline())

for i in range(num):
    data = int(sys.stdin.readline())
    if data == 0:
        if len(heap)!=0:
            output = heapq.heappop(heap)
            print(output[1])
        else:
            print('0')
    else:
        heapq.heappush(heap,[abs(data),data])



