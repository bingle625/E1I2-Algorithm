# 6236번 용돈관리

import sys


N,M = map(int, input().split())
ar = []

for _ in range(N):
    ar.append(int(sys.stdin.readline().rstrip()))

start = max(ar)
end = start*N

while start <= end:
    mid = (start + end ) // 2
    number = 1
    local_money = mid
    
    for i in range(N):
        if local_money - ar[i] >= 0:
            local_money -= ar[i]
        else:
            local_money = mid
            local_money -= ar[i]
            number += 1
    
    if number <= M:
        end = mid - 1
    else:
        start = mid + 1

print(start)