#1697번 숨바꼭질

import collections
import sys


N, K  = map(int, input().split())
graph = collections.defaultdict([])

for i in range(N, K):
    if i-1 >= N-1:
        graph[i].append(i-1)
    if i+1 <=K+1:
        graph[i].append(i+1)
    if i % 2 == 0 and i //2 >= N//2:
        graph[i].append(i//2)
        
def goRoad(number,gr):