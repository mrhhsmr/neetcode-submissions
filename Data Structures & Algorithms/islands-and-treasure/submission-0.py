class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visit = set()
        def update(i, j):
            if i < 0 or j < 0 or i > len(grid) - 1 or \
                j > len(grid[0]) -1 or grid[i][j] == -1:
                return
            
            if (i, j) in visit:
                return
            
            visit.add((i, j))
            q.append([i, j])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visit.add((i, j))

        dist = 0
        while q:
            for i in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist
                update(i + 1, j)
                update(i, j + 1)
                update(i - 1, j)
                update(i, j - 1)
            dist += 1
