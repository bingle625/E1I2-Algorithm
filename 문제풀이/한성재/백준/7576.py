# 7576번 토마토

from collections import defaultdict, deque
import sys
import copy


def sol():
    M, N = map(int, input().split())
    visited = []
    visited2 = defaultdict()
    cannot = []
    cannot2 = defaultdict()
    total = N*M

    for i in range(N):
        arr = list(map(int, sys.stdin.readline().rstrip().split()))
        for k in range(M):
            if arr[k] == 1:
                visited2[(k, i)] = True
            elif arr[k] == -1:
                cannot2[(k, i)] = True
            else:
                pass

    if len(visited) == total - len(cannot):
        print(0)
        return

    q = deque(list(visited2.keys()))
    stair = -1
    while q:
        q2 = copy.deepcopy(q)
        q.clear()
        stair += 1
        while q2:
            nextElem = q2.popleft()
            if nextElem[0]-1 >= 0:
                aboutToPut = (nextElem[0]-1, nextElem[1])
                if aboutToPut not in visited2 and aboutToPut not in cannot2:
                    visited2[aboutToPut] = True
                    q.append(aboutToPut)
            if nextElem[0]+1 < M:
                aboutToPut = (nextElem[0]+1, nextElem[1])
                if aboutToPut not in visited2 and aboutToPut not in cannot2:
                    visited2[aboutToPut] = True
                    q.append(aboutToPut)
            if nextElem[1]-1 >= 0:
                aboutToPut = (nextElem[0], nextElem[1]-1)
                if aboutToPut not in visited2 and aboutToPut not in cannot2:
                    visited2[aboutToPut] = True
                    q.append(aboutToPut)
            if nextElem[1]+1 < N:
                aboutToPut = (nextElem[0], nextElem[1]+1)
                if aboutToPut not in visited2 and aboutToPut not in cannot2:
                    visited2[aboutToPut] = True
                    q.append(aboutToPut)

    if len(visited2) == total - len(cannot2):
        print(stair)
    else:
        print(-1)


sol()
