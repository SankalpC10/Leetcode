class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if m*n !=len(original):
            return res
        for i in range(0,len(original),n):
            arr = original[i:i+n]
            res.append(arr)
        return res


        