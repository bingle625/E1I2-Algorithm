
n = int(input())
minCoin = n+1

for i in range(n//5, -1, -1):
    rest = n - 5*i
    if rest%2 == 0:
        minCoin = i + rest//2
        break
    
if minCoin == n+1:
    print(-1)
else:
    print(minCoin)