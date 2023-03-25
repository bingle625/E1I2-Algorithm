# 절단기 높이 지정: H
# 떡의 개수: N, 손님이 요청한 떡의 길이: M
# idea: 이진탐색으로 최소한의 H값을 array에서 찾고, 그 사이에서 다시 이진탐색?

N, M = map(int, input().split())
array = list(map(int, input().split()))

start, end, mid = 0, N-1, (N-1)//2
array.sort(reverse=True)
result = -1

# 19, 17, 15, 10, 정답 15

def sumDiff(arr, h):
    sum = 0
    for elem in arr:
        sum += elem - h
    return sum

while start < end:
    H = array[mid]
    sum = sumDiff(array[start:mid+1], H)

    if sum == M:
        print(H)
        break
    if sum > M:
        if M-result > M-sum:
            result = sum
            print(result)
            break
        end = mid-1
        mid = end//2
    else:
        mid = (mid+end)//2

