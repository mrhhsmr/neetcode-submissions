class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        mp = {}
        for i in range(numCourses):
            mp[i] = []
        
        for crs, pre in prerequisites:
            mp[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        total = 0
        while q:
            curr = q.popleft()
            total += 1
            for nextCrs in mp[curr]:
                indegree[nextCrs] -= 1
                if indegree[nextCrs] == 0:
                    q.append(nextCrs)
    
        return total == numCourses
        


