# from collections import deque
# # def find_one(target, nums):
# #     nums_queue = deque()
# #     idx = 0
# #     nums_queue.append((target, idx))
# #     while len(nums_queue) and idx < len(nums)-1:
# #         target, idx = nums_queue.popleft()
# #         if target == nums[idx]:
# #             return True
# #         idx += 1
# #         if target>nums[idx]:
# #             nums_queue.append((target-nums[idx], idx))
# #         nums_queue.append((target, idx))
# #     return False
    
            
# def is_solution(queue1, queue2):
#     all_queue = queue1+queue2
#     sum_queue = sum(all_queue)
#     if sum_queue%2 != 0:
#         return False
#     if find_one(sum_queue/2, all_queue):
#         return True
#     else:
#         return False
    
# def solution(queue1, queue2):
#     all_len = len(queue1)*2
#     queue1 = deque(queue1)
#     queue2 = deque(queue2)
#     cnt = 0
#     while True:
#         sum_queue1 = sum(queue1)
#         sum_queue2 = sum(queue2)

#         if sum_queue1 > sum_queue2:
#             num = queue1.popleft()
#             queue2.append(num)
#         elif sum_queue1 < sum_queue2:
#             num = queue2.popleft()
#             queue1.append(num)
#         else:
#             break
#         cnt += 1     
#         if cnt > all_len:
#             return -1
        
#     return cnt

# queue1 과 queue2의 합을 비교한다
# 매번 합을 비교하는 것은 시간 초과
# 따라서 아래와 같이 투포인터 방식을 사용한다

from collections import deque
    
    
def solution(queue1, queue2):
    queue3 = queue1+queue2
    cnt = 0
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    if (sum_queue1+sum_queue2) % 2 != 0:
        return -1
    target = (sum_queue1+sum_queue2)/2
    start = 0
    end = len(queue1)-1
    all_len = len(queue3)
    while True:
        if sum_queue1 > target:
            num = queue3[start]
            sum_queue1 -= num
            start += 1
        elif sum_queue1 < target:
            if end >= all_len-1:
                return -1
            num = queue3[end+1]
            sum_queue1 += num
            end += 1
        else:
            return cnt
        cnt += 1     
        
    return cnt