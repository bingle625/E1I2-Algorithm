import sys
from sys import stdin
sys.setrecursionlimit(10**5)


def findway(lst: list, i, j):

    if i < 0 or j < 0 or j >= len(lst[i]):
        return 0

    if lst[i][j] == 1:
        if i == 0:
            return 1
        else:
            return findway(lst, i-1, j+1) + findway(lst, i-1, j) + findway(lst, i-1, j-1)
    else:
        return 0


n, m = list(map(int, stdin.readline().split()))
board = []
for i in range(n):
    board.append(list(map(int, stdin.readline().split())))


sum = 0
for i in range(len(board[0])):
    sum += findway(board, n-1, i)


print(sum)
