class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        minCol = 0
        maxCol = len(mat) - 1
        
        while(minCol <= maxCol):
            midCol = (int)((minCol + maxCol) / 2)
            maxRow = 0
            
            for row in range(len(mat[0])):
                maxRow = row if mat[midCol][row] > mat[midCol][maxRow] else maxRow
            
            if midCol > 0 and mat[midCol - 1][maxRow] > mat[midCol][maxRow]:
                maxCol = midCol - 1
            elif midCol + 1 < len(mat) and mat[midCol + 1][maxRow] > mat[midCol][maxRow]:
                minCol = midCol + 1
            else:
                return [midCol, maxRow]