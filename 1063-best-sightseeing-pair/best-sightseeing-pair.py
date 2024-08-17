class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_diff, curr =0,0
        for i in range(1, len(values)):
            curr = max(curr, values[i-1] + i-1)
            max_diff = max(max_diff, curr+values[i]-i)
        return max_diff