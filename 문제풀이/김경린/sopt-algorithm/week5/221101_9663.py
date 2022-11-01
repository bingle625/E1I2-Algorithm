from sys import stdin

n = int(stdin.readline())

queen = []

def is_checked(x,y):
    for i,j in queen:
        if i == x or j == y or abs(x-i) == abs(y-j):
            return True
    return False

arr = [[0 for _ in range(n)] for _ in range(n)]

def nqueens(x,cnt):
    if x == n-1:
        cnt += 1
        return cnt
    for i in range(n):
        if not is_checked(x+1,i):
            queen.append((x+1,i))
            cnt = nqueens(x+1,cnt)
            queen.pop()
    return cnt
cnt = 0
cnt = nqueens(-1,cnt)
print(cnt)