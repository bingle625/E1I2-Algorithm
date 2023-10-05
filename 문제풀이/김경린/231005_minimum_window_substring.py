class Solution:
    def is_same(self, dict1, dict2):
        for key in dict2:
            if key not in dict1 or dict1[key] < dict2[key]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:

        start_idx = 0
        fin_idx = len(s)-1
        min_start = 0
        min_fin = len(s)
        nums = {}
        t_nums = {}
        for char in t:
            if char in t_nums:
                t_nums[char] += 1
            else:
                t_nums[char] = 1
        
        for idx, val in enumerate(s):
            if val not in t_nums.keys():
                continue
            if val in nums:
                nums[val] += 1
            else:
                nums[val] = 1
            
            if self.is_same(nums, t_nums):
                start = start_idx
                while s[start] not in t_nums or nums[s[start]] > t_nums[s[start]]:
                    if s[start] in t_nums:
                        nums[s[start]] -= 1
                    start += 1
                start_idx = start
                fin_idx = idx

                if (min_fin - min_start) > fin_idx-start_idx:
                    min_start = start_idx
                    min_fin = fin_idx 

        return s[min_start:min_fin+1] if min_fin != len(s) else ""