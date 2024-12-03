class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        for i in range(len(spaces)):
            if i==0:
                start=0
            else:
                start=spaces[i-1]
            end=spaces[i]
            res+=s[start:end]
            res+=" "
        res+=s[spaces[-1]:]
        return res
