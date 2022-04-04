class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i+1]-prices[i],0) for i in range(len(prices)- 1))
        # result = 0
        # for i in range(len(prices) -1 ):
        #     if prices[i + 1] > prices[i]:
        #         result += prices[i+1] - prices[i]
        # return result