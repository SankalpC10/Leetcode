class Solution:
    def reverseWords(self, s: str) -> str:
        l = [i for i in s.split()]
        l = l[::-1]
        res = " ".join(i for i in l)
        return res
