from collections import deque


N = int(input())
M = int(input())
S = input()
tar = "IOI"
sum = 0

if N - 1 > 0:
    tar = tar + ("OI" * (N-1))



for i in range(2*N+1 ):
    if S.startswith(tar):
        sum += 1
    S = S[1:]

print(sum)