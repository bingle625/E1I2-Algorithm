from collections import defaultdict
def solution(lottos, win_nums):
    lottos_dict = defaultdict(int)
    for lotto in lottos:
        lottos_dict[lotto] += 1
    right = 0
    for num in win_nums:
        if lottos_dict[num] == 1:
            right += 1

    rank = [6,6,5,4,3,2,1]
    answer = [rank[right+lottos_dict[0]], rank[right]]
    # good_rank = 7-(right+lottos_dict[0])if (right+lottos_dict[0]) > 1 else 6
    # bad_rank = 7-right if right > 1 else 6 
    # answer = [good_rank, bad_rank]
    return answer
