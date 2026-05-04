class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            if s1 != s2:
                heapq.heappush(heap, -(abs(s1) - abs(s2)))
        
        return -heap[0] if len(heap) else 0