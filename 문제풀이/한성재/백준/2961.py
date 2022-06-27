# 도영이가 만든 맛있는 음식

import sys
from itertools import combinations

number = int(input())
arr = []

for i in range(number):
    S, B = map(int, sys.stdin.readline().strip().split())
    arr.append((S, B))

coms = [list(combinations(range(number), i)) for i in range(1, number+1)]

mini = sys.maxsize

for item in coms:
    for elem in item:
        s, b = 1, 0
        for number in elem:
            s *= arr[number][0]
            b += arr[number][1]
        mini = min(mini, abs(s-b))


print(mini)
