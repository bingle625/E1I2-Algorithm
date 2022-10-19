import itertools


N, M = map(int,input().split())

numbers = []

for i in range(N):
    numbers.append(i+1)

p = list(itertools.permutations(numbers,M))

for i in range(len(p)):
    for k in range(M):
        print(p[i][k],end=" ")
    print()
    