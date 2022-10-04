number = int(input())

horrors = list(map(int, input().rstrip().split()))

horrors.sort()

cnt = 0
member = 0

for mem in horrors:
    member += 1
    
    if member >= mem:
        member = 0
        cnt += 1

print(cnt)

