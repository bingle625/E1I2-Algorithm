class Solution(object):
    def search(self, nums, target):
       try:
           return nums.index(target)
        except ValueError:
            return -1
        