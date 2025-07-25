class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positive_nums_set = set([num for num in nums if num >0])
        return max(nums) if len(positive_nums_set) == 0 else sum(positive_nums_set)
