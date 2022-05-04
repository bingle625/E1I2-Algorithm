from bisect import bisect


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        
        result = 0
        for i in s:
            # 이진 검색으로 더 큰 인덱스 탐색
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1
        return result
        
        
        # g.sort()
        # s.sort()
        
        # child_i = cookie_j = 0
        # #만족하지 못할 때까지 그리디 진행
        
        # while child_i < len(g) and cookie_j < len(s):
        #     if s[cookie_j] >= g[child_i]:
        #         child_i += 1
        #     cookie_j += 1
        
        # return child_i
        
        