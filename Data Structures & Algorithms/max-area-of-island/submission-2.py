class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, self.dfs(i, j, grid))
        
        return res
    
    def dfs(self, i: int, j :int, grid: List[List[int]]) -> int:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        
        if grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0
        
        return 1 + self.dfs(i - 1, j ,grid) + self.dfs(i, j - 1, grid) + \
                self.dfs(i + 1, j, grid) + self.dfs(i, j + 1, grid)
                