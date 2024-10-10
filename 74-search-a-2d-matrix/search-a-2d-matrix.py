class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        for i in range(len(matrix)):
            if target<=matrix[i][-1]:
                left,right = 0,n-1
                while left<=right:
                    mid = (left+right)//2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid]<target:
                        left = mid+1
                    else:
                        right = mid-1
        return False