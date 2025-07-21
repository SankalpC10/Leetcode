class Solution:
    def makeFancyString(self, s: str) -> str:
        temp=[]
        for i in s:
            if len(temp)>1:
                if temp[-1]==temp[-2]==i:
                    continue
            temp.append(i)
        res ="".join(i for i in temp)
        return res
            
            
                

            
