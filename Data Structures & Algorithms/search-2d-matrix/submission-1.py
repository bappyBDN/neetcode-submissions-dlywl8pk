class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        l=0
        r=(col)-1
        while l < row and r>=0:
            mid=l+r//2
            if matrix[l][r] > target:
                r-=1
            elif matrix[l][r]< target:
                l+=1
            else:
                return True
        return False


        