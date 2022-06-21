# 18870
import heapq
import sys


number = int(input())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

arrSet = set(arr)
arrSet = list(arrSet)
dic = dict()

x = 0
heapq.heapify(arrSet)

while arrSet:
    dic[heapq.heappop(arrSet)] = x
    x += 1

for item in arr:
    print(dic[item], end=' ')
