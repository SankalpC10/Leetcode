class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index, n = 0,len(nums)
        for i in range(n):
            if nums[i]!= 0:
                nums[non_zero_index],nums[i] = nums[i],nums[non_zero_index]
                non_zero_index += 1
        
        