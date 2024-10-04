class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, max_p = prices[0],0
        for i in prices:
            max_p = max(i-lowest, max_p)
            lowest = min(i,lowest)
        return max_p
