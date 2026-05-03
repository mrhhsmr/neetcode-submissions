class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = {}
        for i in range(numCourses):
            mp[i] = []

        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            mp[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        total = 0
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            total += 1
            for nextCrs in mp[curr]:
                indegree[nextCrs] -= 1
                if indegree[nextCrs] == 0:
                    q.append(nextCrs)
        
        if total != numCourses:
            return []

        return res



            


            