class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        max_width = 0
        
        for j in range(n-1,-1,-1):
            while stack and nums[stack[-1]] <= nums[j]:
                max_width = max(max_width, j-stack[-1])
                stack.pop()
        return max_width