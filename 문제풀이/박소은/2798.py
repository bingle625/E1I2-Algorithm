
n, m = map(int, input().split())
cards = list(map(int, input().split()))

maxNum = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            cardSum = cards[i] + cards[j] + cards[k]
            if cardSum <= m and cardSum > maxNum:
                maxNum = cardSum

print(maxNum)