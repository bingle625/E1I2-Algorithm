# 2630번 색종이 만들기
from typing import Counter
from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)


N = int(input())
arr = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]

numbers = Counter({1: 0, 0: 0})


def dore(sR, eR, sH, eH):
    a = arr[sR][sH]

    for i in range(sR, eR):
        for j in range(sH, eH):
            if arr[i][j] != a:
                dore(sR, eR//2, sH, eH//2)
                dore(eR//2, eR, sH, eH//2)
                dore(sR, eR//2, eH//2, eH)
                dore(eR//2, eR, eH//2, eH)

    numbers[a] += 1
    return


dore(0, N, 0, N)

print(numbers[0])
print(numbers[1])
