# N: 나의 현재 위치, K: 동생의 현재 위치
# 나는 X-1(1초), X+1(1초), 2*X(0초)로 이동 가능
import collections
import heapq

N, K = map(int, input().split())

# 큐 변수: [(소요 시간, 위치)]
Q = [(0, N)]
dist = collections.defaultdict(int)
dist[N] = 0

while Q:
    time, locate = heapq.heappop(Q)
    if locate == K:
        print(time)
        break
    elif locate*2 <= 100000 and 2*locate not in dist:
        dist[2*locate] = time
        heapq.heappush(Q, (time, 2*locate))
    if locate+1 <= 100000 and locate+1 not in dist:
        dist[locate+1] = time+1
        heapq.heappush(Q, (time+1, locate+1))
    if locate-1 >= 0 and locate-1 not in dist:
        dist[locate-1] = time+1
        heapq.heappush(Q, (time+1, locate-1))