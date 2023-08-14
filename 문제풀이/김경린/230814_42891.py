from collections import deque
import heapq
# def solution(food_times, k):
#     idx = 0
#     while k > 0:
#         food_times[idx] -= 1
#         k -= 1
#         idx = (idx + 1)%len(food_times)
#         while food_times[idx] == 0:
#             idx = (idx + 1)%len(food_times)
        
#     while food_times[idx] == 0:
#         idx = (idx + 1)%len(food_times)
#     return idx + 1


# # 효율성 테스트 실패
# def solution(food_times, k):
#     idxs = deque([i for i in range(len(food_times))])
#     idx = 0
    
#     while k > 0 and len(idxs):
#         idx = idxs.popleft()
#         food_times[idx] -= 1
#         k -= 1
#         if food_times[idx] > 0:
#             idxs.append(idx)
#     if len(idxs) == 0:
#         return -1
#     else:
#         return idxs[0] + 1


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    foods = []
    for idx in range(len(food_times)):
        heapq.heappush(foods, (food_times[idx], idx))
    
    prev = 0
    while k >= 0:
        time = (foods[0][0] - prev) * len(foods)
        if time <= k:
            k -= time
            prev, _ = heapq.heappop(foods)
        else:
            idx = k%len(foods)
            foods.sort(key=lambda x:x[1])
            idx = foods[idx][1]
            break
    return idx + 1
            
