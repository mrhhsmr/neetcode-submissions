class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        for i in range(len(heights)):
            self.dfs(i, 0, heights, heights[i][0], pac)
            self.dfs(i, len(heights[0]) - 1, heights, heights[i][len(heights[0]) - 1], atl)
        
        for j in range(len(heights[0])):
            self.dfs(0, j, heights, heights[0][j], pac)
            self.dfs(len(heights) - 1, j, heights, heights[len(heights) - 1][j], atl)

        res = list()
        for (r, c) in pac:
            if (r,c ) in atl:
                res.append((r,c))
        
        return res


    def dfs(self, i : int, j: int, heights, prevHeight, visit):
        if((i, j) in visit or i < 0 
        or j < 0 or i >= len(heights) or j >= len(heights[0])
        or heights[i][j] < prevHeight):
            return

        visit.add((i, j))
        self.dfs(i + 1, j, heights, heights[i][j], visit) 
        self.dfs(i - 1, j, heights, heights[i][j], visit) 
        self.dfs(i, j + 1, heights, heights[i][j], visit) 
        self.dfs(i, j - 1, heights, heights[i][j], visit) 