from typing import List

# Solution 1
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Solution 2: Using dictionary
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in dict:
                return [i, dict[x]]
            dict[num] = i
        return []