class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        close_num = nums[0]
        for i in nums:
            if abs(i)<abs(close_num):
                close_num = i
        if close_num <5 and abs(close_num) in nums:
            return abs(close_num)
        return close_num
            