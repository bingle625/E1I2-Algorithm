
import heapq
import sys

case = int(input())

conf = []

for i in range(case):
    start,finish = map(int,input().split())
    heapq.heappush(conf,(start,finish))

cnt = 0
bf_finish = 0

while len(conf):
    start,finish = heapq.heappop(conf)
    while len(conf) and conf[0][0]<finish and start>=bf_finish:
        tmp = heapq.heappop(conf)
        if tmp[1] < finish:
            start,finish = tmp[0],tmp[1]

    bf_finish = finish
    cnt += 1

print(cnt)