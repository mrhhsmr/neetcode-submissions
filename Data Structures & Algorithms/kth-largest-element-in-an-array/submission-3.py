class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.append(-num)

        heapq.heapify(heap)
        while k - 1 > 0:
            heapq.heappop(heap)
            k -= 1
        
        return -heap[0]
