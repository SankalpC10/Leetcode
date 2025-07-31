class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N,M = len(text1),len(text2)
        cache = [[-1]*M for _ in range(N)]
        return self.memoHelper(text1,text2,0,0,cache)

    def memoHelper(self,text1,text2,i1,i2,cache):
        if i1 == len(text1) or i2 == len(text2):
            return 0
        if cache[i1][i2]!= -1:
            return cache[i1][i2]
        if text1[i1]==text2[i2]:
            cache[i1][i2]=1+self.memoHelper(text1,text2,i1+1,i2+1,cache)
        else:
            cache[i1][i2] = max(self.memoHelper(text1,text2,i1+1,i2,cache),self.memoHelper(text1,text2,i1,i2+1,cache))
        return cache[i1][i2]
