class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        curr = 1
        for i in range(0,len(nums)):
            ans[i] *= curr
            curr *= nums[i]
        curr = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= curr
            curr *=nums[i]
        return ans
        
                




            
                