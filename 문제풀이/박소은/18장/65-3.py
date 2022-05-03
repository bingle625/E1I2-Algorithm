import bisect

class Solution(object):
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
