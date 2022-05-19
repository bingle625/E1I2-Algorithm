# 2630번 색종이 만들기
from typing import Counter
from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)


N = int(input())
arr = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]

numbers = Counter({1: 0, 0: 0})


def dore(x, y, N):
    a = arr[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if arr[i][j] != a:
                dore(x, y, N//2)
                dore(x, y+N//2, N//2)
                dore(x+N//2, y, N//2)
                dore(x+N//2, y+N//2, N//2)
                return

    numbers[a] += 1
    return


dore(0, 0, N)

print(numbers[0])
print(numbers[1])
