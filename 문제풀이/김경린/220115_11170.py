def count_zero(start, end):
    cnt = 0
    for i in range(start, end+1):
        for x in str(i):
            if x == "0":
                cnt += 1
    print(cnt)


case = int(input())
for i in range(case):
    start, end = map(int, input().split())
    count_zero(start, end)
