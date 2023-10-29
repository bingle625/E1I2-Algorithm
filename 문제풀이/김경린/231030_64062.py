# def find_next_start_idx(max_idx, stones, k, cross_num):
#     for idx in range(max_idx+1, len(stones)-k+1):
#                 if stones[idx] < cross_num:
#                     return idx
#     return float('inf')
                    

# def solution(stones, k):
#     answer = 0
#     start_idx = 0
#     cross_num = float('inf')
#     for i in range(len(stones)-k+1):
#         if i == start_idx:
#             max_val = stones[i]
#             max_idx = i
#             for j in range(i+1, i+k):
#                 if max_val < stones[j]:
#                     max_idx = j
#                     max_val = stones[j]
                
#             if max_val<cross_num:
#                 cross_num = max_val
            
#             start_idx = find_next_start_idx(max_idx, stones, k, cross_num)
            
    

                    
                
#     return cross_num


def solution(stones, k):
    set_stones = sorted(set(stones))
    s, f = set_stones[0], set_stones[-1]
    answer = 0
    while s <= f :
        mid = (s + f)//2
        cnt = 0
        steps = []
        for i in range(len(stones)):
            if stones[i] < mid:
                cnt += 1 # 건너 뛴 것 개수
            else:
                steps.append(cnt)
                cnt = 0
        steps.append(cnt)
        max_steps = max(steps)
        if max_steps < k:
            answer = mid
            s = mid + 1
        else:
            f = mid - 1
    return answer
                
        
        