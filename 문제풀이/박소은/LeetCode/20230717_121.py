class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10000
        profit = 0

        for price in prices:
            min_price = min(min_price, price)    # 최저값 찾기
            profit = max(profit, price-min_price)    # 최대수익

        return profit