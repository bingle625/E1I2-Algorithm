#2751 수정렬하기 2

import sys


number = int(input())

numList = []

for _ in range(number):
    numList.append(int(sys.stdin.readline().rstrip()))

numList.sort()

for number in numList:
    print(number)