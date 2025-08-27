class Solution:
    def trap(self, height: List[int]) -> int:
        L,R = 0,len(height)-1
        max_L,max_R = height[0],height[-1]
        trapped_water = 0
        while L<R:
            max_L = max(max_L,height[L])
            max_R = max(max_R,height[R])
            trapped_water += max_L-height[L]
            trapped_water += max_R-height[R]
            if max_L<=max_R:
                L+=1
            else:
                R-=1
        return trapped_water 