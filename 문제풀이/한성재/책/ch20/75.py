


import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #풀이 2. 큐를 이용한 최적화
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i,v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            #새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v
            
            results.append(current_max)
            
            #최댓값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = float('inf')
        return results
        
        # # 풀이 1. 브루트포스로 계산
        # if not nums:
        #     return nums
        
        # r = []
        # for i in range(len(nums)- k +1):
        #     r.append(max(nums[i:i+1]))
        # return r
        
s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))