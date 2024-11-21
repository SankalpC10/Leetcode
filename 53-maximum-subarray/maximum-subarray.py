class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_overall,max_ending_here = nums[0],0
        for num in nums:
            max_ending_here +=num
            max_overall = max(max_overall, max_ending_here)
            if max_ending_here <0:
                max_ending_here = 0

        return max_overall