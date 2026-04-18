class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev_n = str(n)[::-1]
        return(abs(int(rev_n)- n))
        