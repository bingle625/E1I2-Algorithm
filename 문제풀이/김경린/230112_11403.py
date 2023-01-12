from collections import defaultdict
from operator import truediv


n = int(input())

v = []
for i in range(n):
    v_ = list(map(int, input().split()))
    v.append(v_)


for k in range(n):
    for i in range(n):
        for j in range(n):
            if v[i][k] and v[k][j]:
                v[i][j] = 1

for i in range(n):
    for j in range(n):
        print(v[i][j], end=' ')
    print('')
