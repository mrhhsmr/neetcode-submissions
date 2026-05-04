class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1
        
        res = 0
        while len(q) > 0 and fresh > 0:
            size = len(q)           
            for i in range(size):
                ci, cj = q.popleft()
                if ci > 0 and grid[ci - 1][cj] == 1:
                    grid[ci - 1][cj] = 2
                    fresh -= 1
                    q.append([ci - 1, cj])
                if ci < len(grid) -1 and grid[ci + 1][cj] == 1:
                    grid[ci + 1][cj] = 2
                    fresh -= 1
                    q.append([ci + 1, cj])
                if cj > 0 and grid[ci][cj - 1] == 1:
                    grid[ci][cj - 1] = 2
                    fresh -= 1
                    q.append([ci, cj - 1])
                if cj < len(grid[0]) -1 and grid[ci][cj + 1] == 1:
                    grid[ci][cj + 1] = 2
                    fresh -= 1
                    q.append([ci, cj + 1])
            res += 1
            
        return -1 if fresh > 0 else res