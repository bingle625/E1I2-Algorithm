from sys import stdin

n = int(stdin.readline())

row = [ 0 for _ in range(n)]

def is_checked(x):
    for i in range(x):
        if row[i] == row[x] or abs(x-i) == abs(row[x]-row[i]):
            return True
    return False

def nqueens(x):
    global cnt
    if x == n:
        cnt += 1
        return
    for i in range(n):
        row[x] = i
        if not is_checked(x):
            nqueens(x+1)

cnt = 0
nqueens(0)
print(cnt)