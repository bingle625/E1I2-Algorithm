
import collections

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []

    # 힙에 음수로 삽입
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = list()

    # k번 만큼 추출, 최소 힙이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
        topk.append(heapq.heappop(freqs.heap)[1])

    return topk