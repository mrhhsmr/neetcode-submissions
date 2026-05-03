class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = {}
        for i in range(numCourses):
            mp[i] = []
        
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            mp[pre].append(crs)
            indegree[crs] += 1

        res = []
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        total = 0
        while q:
            crs = q.popleft()
            res.append(crs)
            total += 1
            for nextCrs in mp[crs]:
                indegree[nextCrs] -= 1
                if indegree[nextCrs] == 0:
                    q.append(nextCrs)
        
        if total != numCourses:
            return[]
            
        return res

            


            