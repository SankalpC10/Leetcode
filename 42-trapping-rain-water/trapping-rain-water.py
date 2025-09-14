class Solution:
    def trap(self, height: List[int]) -> int:
        L,R =  0,len(height)-1
        maxL,maxR = height[L],height[R]
        trapped = 0
        while L<R:
            if maxL<maxR:
                L+=1
                maxL = max(maxL,height[L])
                trapped += maxL-height[L]
            else:
                R-=1
                maxR = max(maxR,height[R])
                trapped += maxR-height[R]
        return trapped
