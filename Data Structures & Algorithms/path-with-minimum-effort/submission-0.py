class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        # [diff, row ,col]
        heap = [[0,0,0]]
        visited = set()
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while heap:
            diff, r, c = heapq.heappop(heap)
            if (r,c) in visited:
                continue
            
            visited.add((r, c))
            if (r, c) == (rows - 1, cols - 1):
                return diff
            
            for dr, dc in direction:
                newR = r + dr
                newC = c + dc
                if newR < 0 or newC < 0 or newR >= rows or newC >= cols:
                    continue
                
                if (newR, newC) in visited:
                    continue
                
                newDiff = max(diff, abs(heights[newR][newC] - heights[r][c]))
                heapq.heappush(heap, [newDiff, newR, newC])
        
        return 0