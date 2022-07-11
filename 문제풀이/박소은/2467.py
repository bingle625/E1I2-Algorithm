# N: 전체 용액의 수, liquid는 오름차순으로 입력된다.
import sys
MAX = 1000000001
MIN = -MAX

N = int(input())
liquid = list(map(int, input().split()))

a = 0   # 작은 값의 인덱스
b = N-1  # 큰 값의 인덱스
answer = [liquid[a], liquid[b]]

while a < b:
    diff = abs(liquid[b] + liquid[a])    # a와 b의 차이값
    if diff < abs(answer[0]+answer[1]):
        answer[0] = liquid[a]
        answer[1] = liquid[b]

    if liquid[b]+liquid[a] > 0:
        b -= 1
    elif liquid[b]+liquid[a] < 0:
        a += 1
    else:
        break

print(answer[0], answer[1])