import collections


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        
        freqs = collections.Counter(S)
        count = 0
        
        for char in J:
            count += freqs[char]
        
        return count