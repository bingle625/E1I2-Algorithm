# 프로젝트 매니징

N = int(input())
T, M = map(int, input().split())
time = T*60 + M

for _ in range(N):
    time += int(input())

T = time//60
while T >= 24:
    T -= 24

print(T, time%60)