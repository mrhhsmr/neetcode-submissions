class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mp = {}
        for source, dest, price in flights:
            if source not in mp:
                mp[source] = []
            mp[source].append([dest, price])
        
        minHeap = [(0, src, -1)] # cost, node, stops
        best = {}
        best[(src, -1)] = 0
        while len(minHeap):
            cst, node, stops = heapq.heappop(minHeap)
            if node == dst:
                return cst
            
            # cannot fly anymore
            if stops == k:
                continue
            
            for nextS, price in mp.get(node, []):
                newCost = cst + price
                newStop = stops + 1
                if newCost < best.get((nextS, newStop), float('inf')):
                    best[(nextS, newStop)] = newCost
                    heapq.heappush(minHeap, (newCost, nextS, newStop))

        
        return -1
        

        