number = int(input())

horrors = sorted(list(map(int, input().split())))

cnt = 0
res = 1

for i in horrors:
    if i > cnt:
        cnt += 1
    else:
        cnt = 0
        res += 1

print(res)
