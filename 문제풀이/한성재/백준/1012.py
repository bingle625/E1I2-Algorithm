# 1012번 유기농 배추

from collections import deque
from sys import stdin



testCase = int(input())

for _ in range(testCase):
    M, N, K = map(int, stdin.readline().rstrip().split())
    wormPlace = dict([])
    island = 0
    for i in range(K):
        x, y = map(int, stdin.readline().rstrip().split())
        wormPlace[(x,y)] = True
    
    for i in range(M):
        for j in range(N):
            if (i,j) in wormPlace:
                island += 1
                stack = deque([(i,j)])
                while stack:

                    if stack[0] in wormPlace:
                        a, b = stack[0][0], stack[0][1]
                        wormPlace.pop(stack.popleft())
                        stack.append((a+1,b))
                        stack.append((a-1,b))
                        stack.append((a,b+1))
                        stack.append((a,b-1))
                    else:
                        stack.popleft()
    print(island)