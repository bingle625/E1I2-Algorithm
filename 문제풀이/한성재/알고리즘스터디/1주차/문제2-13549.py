# 13549 - 숨바꼭질 문제
from collections import deque


LIMIT = 100000

N, K = map(int, input().split())
timeArr = [LIMIT] * (LIMIT+1)
discovered = [False] * (LIMIT+1)


def bfs(start):
    timeArr[start] = 0
    discovered[start] = True
    q = deque([start])
    time = 0
    while q:
        now = q.popleft()
        if now == K:
            return timeArr[K]
        if now * 2 <= LIMIT:
            if not discovered[now * 2]:
                timeArr[now * 2] = timeArr[now]
                discovered[now * 2] = True
                q.appendleft(now * 2)
        if now - 1 >= 0:
            if not discovered[now-1]:
                timeArr[now - 1] = timeArr[now] + 1
                discovered[now-1] = True
                q.append(now-1)
        if now + 1 <= LIMIT:
            if not discovered[now+1]:
                timeArr[now+1] = timeArr[now] + 1
                discovered[now+1] = True
                q.append(now+1)


print(bfs(N))
