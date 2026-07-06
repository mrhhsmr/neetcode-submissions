class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indgr = [0] * numCourses
        mp = defaultdict(list)
        for prev, next in prerequisites:
            indgr[next] += 1
            mp[prev].append(next)
        
        q = deque()
        for i in range(numCourses):
            if indgr[i] == 0:
                q.append(i)
        
        total = 0
        while q:
            curr = q.popleft()
            total += 1
            for nextC in mp[curr]:
                indgr[nextC] -= 1
                if indgr[nextC] == 0:
                    q.append(nextC)

        return total == numCourses