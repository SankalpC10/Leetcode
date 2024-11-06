class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res =""
        l1,l2 = len(word1),len(word2)
        curr = 0
        while curr<min(l1,l2):
            res +=word1[curr]
            res +=word2[curr]
            curr+=1
        if l2>l1:
            res+=word2[curr:]
        else:
            res+=word1[curr:]
        return res