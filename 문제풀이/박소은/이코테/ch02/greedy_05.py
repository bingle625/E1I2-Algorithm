# p.315 05. 볼링공 고르기
# 서로 다른 무게의 볼링공 2개를 고를 수 있는 경우의 수

n, m = map(int, input().split())    # 볼링공 개수 N, 공의 최대 무게 M
balls = list(map(int, input().split()))

# 풀이 1: 단순 반복
# result = 0
# for i in range(len(balls)):
#     for j in range(i, len(balls)):
#         if balls[i] != balls[j]:
#             result += 1

# print(result)


# 풀이 2: Counter dict 사용
from collections import Counter

# countBalls = list(enumerate(Counter(balls)))
ballCounter = Counter(balls)
ballList = list(enumerate(ballCounter))

print(ballCounter)
print(ballList)
result = 0
# for idx, ball1 in countBalls:
#     for idx, ball2 in countBalls[idx+1:]:
#         result += 

print(result)