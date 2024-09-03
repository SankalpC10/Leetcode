class Solution:
    def getUnlucky(self, s:str):
        sum = 0
        for i in s:
            sum += int(i)
        return str(sum)


    def getLucky(self, s: str, k: int) -> int:
        string = ''
        for i in s:
            string += str(ord(i)-ord('a')+1)
        while k>0:
            string = self.getUnlucky(string)
            k -=1
        return int(string)