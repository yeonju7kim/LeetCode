class Solution:
    
    rdir = [-1, 1, 0, 0]
    cdir = [0, 0, -1, 1]
    def bfs(self, visit, grid, r, c):
        visit[r][c] = True
        for i in range(4):
            newR = r + self.rdir[i]
            newC = c + self.cdir[i]
            if newR < 0 or newC < 0 or newR >= len(visit) or newC >= len(visit[0]):
                continue
            elif visit[newR][newC] == False and grid[newR][newC] == "1":
                self.bfs(visit, grid, newR, newC)
            
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        row = len(grid)
        col = len(grid[0])
        visit = [[False] * col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                if visit[r][c] == False and grid[r][c] == '1':
                    self.bfs(visit, grid, r, c)
                    ans = ans + 1               
        return ans 