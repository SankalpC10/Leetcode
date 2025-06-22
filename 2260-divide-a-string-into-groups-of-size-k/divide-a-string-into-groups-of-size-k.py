class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        if len(s)%k!=0:
            for i in range(k-(len(s)%k)):
                s+=fill
        cur = ""
        for i in range(len(s)):
            if len(cur)==k:
                res.append(cur)
                cur=""
            cur+=s[i]
        res.append(cur)
        return res

