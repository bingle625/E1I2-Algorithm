# 55번 배열의 k번째 큰 요소

import heapq

# # 풀이 1. heapq 모듈 이용
# def findKthLargest(self, nums: list[int], k: int) -> int:
#     heap = list()
#     for n in nums:
#         heapq.heappush(heap, -n)

#     for _ in range(1, k):
#         heapq.heappop(heap)

#     return -heapq.heappop(heap)

# 풀이 2. heapq 모듈의 heapify 이용


def findKrhLargest(self, nums: list[int], k: int) -> int:
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)

    return heapq.heappop(nums)
