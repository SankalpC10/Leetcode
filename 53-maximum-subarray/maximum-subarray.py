class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, max_ending_here = nums[0],0
        for i in range(len(nums)):
            max_ending_here += nums[i]
            if max_ending_here > max_sum:
                max_sum = max_ending_here
            if max_ending_here <0:
                max_ending_here = 0
        return max_sum