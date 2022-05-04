# 1764번 듣보잡

from sys import stdin


N, M = map(int, input().split())
notLi = []
notSe = []
results = []

for _ in range(N):
    notLi.append(stdin.readline().rstrip())

for _ in range(M):
    notSe.append(stdin.readline().rstrip())

notLi.sort()
notSe.sort()

up = 0
down = 0
number = 0

while up < N and down < M:
    if notLi[up] > notSe[down]:
        down += 1
    elif notLi[up] < notSe[down]:
        up += 1
    else:
        results.append(notLi[up])
        number += 1
        up += 1
        down += 1
        
print(number)

for item in results:
    print(item)