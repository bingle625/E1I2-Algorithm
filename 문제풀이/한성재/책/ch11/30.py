#30번 중복 문자 없는 가장 긴 부분 문자열

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)        
            used[char] = index
        return max_length