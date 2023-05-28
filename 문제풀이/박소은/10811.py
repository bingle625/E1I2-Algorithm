n, m = map(int, input().split())
result = [(i+1) for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    result[i-1:j] = reversed(result[i-1:j])

print(*result)