

from itertools import combinations
import sys
from sys import stdin

def findMin(idxs):
    s = 1
    b = 0
    for idx in idxs:
        s *= sour[idx]
        b += bitter[idx]
    return abs(s - b)

num = int(stdin.readline())
sour = []
bitter = []
minValue = sys.maxsize
for i in range(num):
    s, b = map(int, stdin.readline().split())
    sour.append(s)
    bitter.append(b)

# 브루트 포스
# for i in range(1,num+1):
#     for j in list(combinations([k for k in range(0,num)],i)):
#         minValue = min(minValue,findMin(j))

# 비트 마스크 (combination을 비트마스크로)
# ex) num = 4이면
# 1 ~  10000까지 각각 포함되는 경우, 안되는 경우를 0,1로 표현
# 0111은 idx 0,1,2는 포함 3은 미포함
for i in range(1, 1 << num):
    s = 1
    b = 0
    for j in range(num):
        if i & 1 << j:
            s *= sour[j]
            b += bitter[j]
    minValue = min(minValue,abs(s-b))



print(minValue)
