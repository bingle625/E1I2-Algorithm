# 프로그래머스
from collections import defaultdict

# def is_all_include(jewels_dict, gems):
#     for gem in gems:
#         if jewels_dict[gem] < 1:
#             return False
        
#     return True

def solution(gems):
    answer = []
    start = 0
    end = 0
    min_len = len(gems) + 1
    gems_num = len(set(gems))
    cnt = 0
    min_start = -1
    min_end = -1
    jewels_dict = defaultdict(int)
    
    while end < len(gems):
        jewels_dict[gems[end]] += 1
        if jewels_dict[gems[end]] == 1:
            cnt += 1
            
        if gems[end] == gems[start] and start < end:
            while jewels_dict[gems[start]] > 1:
                jewels_dict[gems[start]] -= 1
                start += 1

        if cnt == gems_num:
            if min_len > end - start + 1:
                min_len = min(min_len, end - start + 1)
                min_start = start
                min_end = end
        end += 1

    
        
    return [min_start+1, min_end+1]
