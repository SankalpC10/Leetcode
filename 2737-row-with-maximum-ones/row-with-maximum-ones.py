class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rowInd, maxOne = 0,0
        for i,row in enumerate(mat):
            countOne = 0
            for entry in row:
                if entry == 1:
                    countOne += 1
            if countOne>maxOne:
                maxOne = countOne
                rowInd = i
        return [rowInd,maxOne]
