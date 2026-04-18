class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp_n = n
        rev = 0
        while temp_n >0:
            reminder = temp_n%10
            rev = (rev*10)+reminder
            temp_n = temp_n//10
        return abs(rev-n)
        