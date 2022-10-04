# p.314 04. 만들 수 없는 금액 ***
# N개의 동전으로 만들 수 없는 양의 정수

n = int(input())
coins = list(map(int, input().split()))

# 풀이 1: 교과서 풀이
coins.sort()    # [1, 1, 3, 9]
target = 1
for coin in coins:
    if target < coin:
        break
    target += coin
print(target)