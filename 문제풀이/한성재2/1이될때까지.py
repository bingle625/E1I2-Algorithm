a, b = map(int, input().split())

cnt = 0

while a != 1:
    cnt += 1
    if a % b == 0:
        a //= b
    else:
        a -= 1

print(cnt)
