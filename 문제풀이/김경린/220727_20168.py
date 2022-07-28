import math


row, col = map(int, input().split())
nums = [[0 for _ in range(col)] for _ in range(row)]
for i in range(row):
    tmp = input()
    for j in range(len(tmp)):
        nums[i][j] = tmp[j]

def isSquared(num):
    num = int(num)
    if math.sqrt(num) == int(math.sqrt(num)):
        return True
    else:
        return False

ans = -1
for i in range(row):
    for j in range(col):
        for k in range(-row,row):
            for l in range(-col,col):
                num = ''
                r , c = i, j
                while 0 <= r <row and 0 <= c < col:
                    num +=nums[r][c]
                    if k == 0 and l == 0:
                        break
                    if isSquared(num):
                        ans = max(int(num), ans)
                    r += k
                    c += l

print(ans)