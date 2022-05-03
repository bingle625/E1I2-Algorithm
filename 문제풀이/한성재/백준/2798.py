#2798 블랙잭

from sys import stdin


N,M = map(int, stdin.readline().rstrip().split())

cards = list(map(int, stdin.readline().rstrip().split()))

approx = 0

for a in range(0,N-2):
    for b in range(a+1,N-1):
        for c in range(b+1,N):
            if M - approx >= M - (cards[a]+cards[b]+cards[c]) >= 0:
                approx = cards[a]+cards[b]+cards[c]
            else:
                continue

print(approx)
