from collections import defaultdict
import copy

def compare_after(current, after):
    sum_char = ''
    if current == after[:len(current)]:
        return len(current)
    else:
        cnt = 0
        for char in current:
            sum_char += char
            cnt += 1
            if sum_char != after[:cnt]:
                return len(sum_char)
def compare_before(current, before):
    sum_char = ''
    if before == current[:len(before)]:
        return len(before) + 1
    else:
        cnt = 0
        for char in current:
            sum_char += char
            cnt += 1
            if sum_char != before[:cnt]:
                return len(sum_char)

def solution(words):
    answer = 0
    words.sort()
    words_dict = defaultdict(int)
    
    answer += compare_after(words[0], words[1])
    
    for i in range(1, len(words)-1):
        answer += max(compare_before(words[i], words[i-1]), compare_after(words[i], words[i+1]))
    answer += compare_after(words[-1], words[-2])
        
    return answer