class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        mp = {}
        for i in range(numCourses):
            mp[i] = []
        
        indegree = [0] * numCourses
        for a, b in prerequisites:
            mp[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        total = 0
        while q:
            cur = q.popleft()
            res.append(cur)
            total += 1
            for nextC in mp[cur]:
                indegree[nextC] -= 1
                if indegree[nextC] == 0:
                    q.append(nextC)
        

        if total != numCourses:
            return []
        
        return res

