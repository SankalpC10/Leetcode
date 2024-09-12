class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ip=[i for i in allowed]
        count =0
        for i in words:
            flag = True
            for j in i:
                if j not in ip:
                    flag = False
            if flag:
                count +=1
        return count