class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for u, v, t in times:
            mp[u].append((v, t))
        
        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            t1, curr = heapq.heappop(minHeap)
            if curr in visit:
                continue
            visit.add(curr)
            t = t1
            for next, t2 in mp[curr]:
                if next not in visit:
                    heapq.heappush(minHeap, (t1 + t2, next))
        
        return t if len(visit) == n else -1