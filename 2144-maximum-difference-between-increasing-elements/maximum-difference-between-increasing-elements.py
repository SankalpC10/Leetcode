class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff,min_ever = 0,nums[0]
        for n in nums:
            max_diff = max(n-min_ever,max_diff)
            min_ever = min(n,min_ever)
        return max_diff if max_diff !=0 else -1
