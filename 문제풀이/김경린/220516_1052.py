#1의 갯수가 물병의 갯수

start, final = map(int,input().split())
cnt = 0

while bin(start).count('1') > final:
    cnt += 1
    start += 1

print(cnt)