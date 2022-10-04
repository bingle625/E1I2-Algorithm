from collections import deque
import heapq

# N = 숫자배열 사이즈
# M = 숫자가 더해지는 총 횟수
# K = 연속하여 최대로 더할 수 있는 숫자
N , M, K = map(int, input().rstrip().split())

numbers = list(map(int, input().rstrip().split()))

numbers.sort()

print(numbers)

first = numbers[-1]
second = numbers[-2]

result = 0
result += (first*K + second) * (M//(K+1))
result += (M % (K+1))*first



print(result)