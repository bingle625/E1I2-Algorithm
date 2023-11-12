import heapq
import sys

n = int(sys.stdin.readline())

length = 0
left = []
right = []
# -4 -3 -2 -1   0 1
for _ in range(n):
    num = int(sys.stdin.readline())
    if length == 0:
        heapq.heappush(left, (-num, num))
        mid = num
        length += 1
        print(mid)
        continue

    if length%2 == 0:
        if mid < num:
            heapq.heappush(right, (num, num))
            move = heapq.heappop(right)[1]
            heapq.heappush(left, (-move, move))
        else:
            heapq.heappush(left, (-num, num))
            
    else:
        if mid < num:
            heapq.heappush(right, (num, num))
        
        else:
            heapq.heappush(left, (-num, num))
            move = heapq.heappop(left)[1]
            heapq.heappush(right, (move, move))
    
    mid = heapq.heappop(left)[1]
    heapq.heappush(left, (-mid, mid))
    print(mid)

    length += 1
        
                





    