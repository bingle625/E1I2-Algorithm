number = int(input())
res = 0
cnt = 14 * 60 + 46 * 14
if number > 3:
    cnt = number * cnt + 3600
else:
    cnt = (number + 1) * cnt

print(cnt)
