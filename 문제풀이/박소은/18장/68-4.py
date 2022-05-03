import bisect

class Solution(object):
    def twoSum(self, numbers, target):
        for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k + 1:]
            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2