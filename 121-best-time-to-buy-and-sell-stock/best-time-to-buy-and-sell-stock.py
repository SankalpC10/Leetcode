class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ever, max_profit = prices[0], -1
        for i in prices:
            max_profit = max(max_profit, i-min_ever)
            min_ever = min(min_ever,i)
        return max_profit