

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

for i in range(1,num+1):
    for j in list(combinations([k for k in range(0,num)],i)):
        minValue = min(minValue,findMin(j))

print(minValue)
