# 풀이 1: list 사용
# 시간 초과

# N = int(input())
# nums = []

# for i in range(1, N + 1):
#     nums.append(i)

# temp = 0
# while len(nums) > 1:
#     nums.pop(0)
#     temp = nums.pop(0)
#     nums.append(temp)

# nums.append(temp)
# nums.pop(0)
# print(nums[0])


# 풀이 2: deque 사용
from collections import deque

N = int(input())
nums = deque()

for i in range(1, N + 1):
    nums.append(i)

temp = 1
while len(nums) > 1:
    nums.popleft()
    temp = nums.popleft()
    nums.append(temp)

print(temp)