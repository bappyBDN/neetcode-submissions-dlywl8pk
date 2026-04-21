class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])
        z_r=set()
        z_c=set()
        for r in range(row):
            for c in range(col):
                if matrix[r][c]==0:
                    z_r.add(r)
                    z_c.add(c)
        for r in range (row):
            for j in range(col):
                if r in z_r or j in z_c:
                    matrix[r][j]=0        
        