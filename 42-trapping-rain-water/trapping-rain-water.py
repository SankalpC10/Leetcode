class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r,res = 0,len(height)-1,0
        left_max,right_max = height[l], height[r]
        while l<r:
            if left_max<right_max:
                
                left_max = max(left_max,height[l])
                res += left_max - height[l]
                l += 1
            else:
                r -= 1
                right_max = max(right_max,height[r])
                res += right_max - height[r]
        return res