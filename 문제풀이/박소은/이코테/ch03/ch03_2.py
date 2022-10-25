# 큰 수의 법칙
# 배열의 크기 N, 더해지는 횟수 M, 연속 K번 허용

n, m, k = map(int, input().split())
numList = list(map(int, input().split())).sort(reverse=True)

answer = 0
count = 0
while True:
    # 연속 k만큼 반복해서 더하기
    for _ in range(k):
        if addNum(numList[0]) == True:
            break
    if addNum(numList[1]) == False:
        break
print(answer)

def addNum(num):
    answer += num
    count += 1
    if count == m:
        return True