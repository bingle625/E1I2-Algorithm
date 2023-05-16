n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
nums.sort()

max_weight = 0
for i in range(len(nums)):
    max_weight = max(max_weight, nums[i] * (len(nums)-i))
