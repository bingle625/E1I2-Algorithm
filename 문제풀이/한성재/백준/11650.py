#11650 좌표 정렬하기

import sys


number = int(input())
numberList = []


for _ in range(number):
    x, y = map(int,sys.stdin.readline().rstrip().split())
    numberList.append((x,y))
    
numberList.sort(key= lambda x: x[1])
numberList.sort(key= lambda x: x[0])

for item in numberList:
    print(item[0],item[1])
