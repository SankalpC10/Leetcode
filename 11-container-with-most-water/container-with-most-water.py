class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l,r = 0,len(height)-1
        while l<r:
            max_area = max(max_area,(r-l)*min(height[l],height[r]))
            if height[r]<height[l]:
                r -=1
            else:
                l +=1
        return max_area
