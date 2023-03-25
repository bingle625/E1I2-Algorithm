from collections import defaultdict
import heapq
def solution(genres, plays):
    answer = []
    genres_cnt = defaultdict(list)
    for i in range(len(plays)):
        heapq.heappush(genres_cnt[genres[i]],(-plays[i],i))
    genres_cnt_heap = []
    for key in genres_cnt:
        sum_cnt = 0
        for play_num,idx in genres_cnt[key]:
            sum_cnt -= play_num
        heapq.heappush(genres_cnt_heap,(-sum_cnt, key))

    while len(genres_cnt_heap):
        val, key = heapq.heappop(genres_cnt_heap)
        for i in range(2):
            if len(genres_cnt[key]):
                num, idx = heapq.heappop(genres_cnt[key])
                answer.append(idx)
        
    return answer