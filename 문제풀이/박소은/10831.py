n, m = map(int, input().split())
result = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    result[i-1], result[j-1] = result[j-1], result[i-1]
print(*result)