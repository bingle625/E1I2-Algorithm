#1978번 소수 찾기
#에라토스테네스의 체
import sys


num = int(input())
got = [2]
sosunum = 0

numArr = list(map(int, sys.stdin.readline().rstrip().split()))

numArr.sort()

for i in range(3,numArr[-1]+1):
    sosu = True
    for g in got:
        if i % g == 0:
            sosu = False
            break
    if sosu:
        got.append(i)
    else:
        continue
    
for number in numArr:
    if number in got:
        sosunum += 1
print(sosunum)