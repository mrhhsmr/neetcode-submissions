class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        
        # 堆里的元素: (distance, point_index)
        # 从 index 0 开始，初始距离为 0
        min_heap = [(0, 0)]
        
        total_cost = 0
        
        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)
            
            # 如果这个点已经在 MST 里了，直接跳过（避免成环/重复计算）
            if u in visited:
                continue
                
            # 把当前最近的点加入 MST
            visited.add(u)
            total_cost += cost
            
            # 扩展：计算 u 到所有其他未访问点的距离，放进堆里
            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (dist, v))
                    
        return total_cost