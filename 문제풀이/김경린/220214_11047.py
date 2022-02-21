
from re import L


n,k = input().split()
n = int(n)
k = int(k)

coins = []
coin_num = 0

for i in range(n):
    tmp = int(input())
    coins.append(tmp)

while True:
    coin = coins.pop()
    if coin<=k:
        coin_num += k//coin
        k -= (k//coin)*coin
        if k==0:
            break
print(coin_num)