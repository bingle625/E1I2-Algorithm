#1697번 숨바꼭질

from collections import deque
import collections


N, K = map(int,input().split())

q1 = deque([N])
subq1 = deque([])
discovered1 = dict([])
number1 = 0

def findN(q,subq,discovered,number):
    while True:
        while q:
            v = q.popleft()
            if v == K:
                return number
            else:
                if v-1>= -1 and v-1 not in discovered:
                    discovered[v-1] = True
                    subq.append(v-1)
                if v+1 <= 100001 and v+1 not in discovered:
                    discovered[v+1] = True
                    subq.append(v+1)
                if v*2 <= 100001 and v*2 not in discovered:
                    discovered[v*2] = True
                    subq.append(v*2)
        
        subq, q = q, subq
        number += 1
        
print(findN(q1,subq1,discovered1,0))