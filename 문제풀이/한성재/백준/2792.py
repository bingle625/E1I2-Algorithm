from sys import stdin


N, M = map(int,input().split())
arr = []

for _ in range(M):
    arr.append(int(stdin.readline().rstrip()))

start = 1
end = max(arr)

while start <= end:
    number = 0
    mid = (start + end) // 2
    
    for i in range(M):
        number += arr[i] // mid
        if arr[i] % mid != 0:
            number += 1
    
    #number이 5명이면, 기준 낮춰야함.
    if number <= N:
        end = mid - 1
    #number이 7명 이상이면 기준 높여야함
    else:
        start = mid + 1

print(start)