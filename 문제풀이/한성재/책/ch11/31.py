# 31번 상위 K 빈도 요소

import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqs = collections.Counter(nums)
        freqs_heap = []
        #힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        
        topk =list()
        # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        
        return topk
    
    
# 파이썬다운 방식 
    class Solution(object):
        def topKFrequent(self, nums, k):
            return list(zip(*collections.Counter(nums).most_common(k)))[0]