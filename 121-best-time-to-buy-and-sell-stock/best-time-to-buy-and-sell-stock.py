class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ever,max_profit = prices[0],0
        for num in prices:
            max_profit = max(max_profit,num-min_ever)
            min_ever = min(min_ever,num)
        return max_profit