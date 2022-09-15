from collections import deque
from sys import stdin

n, value = map(int, stdin.readline().split())
coin = []
for i in range(n):
    v = int(stdin.readline())
    coin.append(v)

num = [0 for _ in range(value+1)]
num[0] = 1
for i in range(len(coin)):
    for j in range(coin[i], value+1):
        if j-coin[i]>=0:
            num[j] += num[j-coin[i]] 

    

print(num[value])
