# 숫자 카드 게임

# 입력 받기
N, M = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

minArray = []
for i in range(N):
    minArray.append(min(array[i]))

print(max(minArray))