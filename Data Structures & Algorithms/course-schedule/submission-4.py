class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        mp = {}
        for i in range(numCourses):
            mp[i] = []
            
        for n, c in prerequisites:
            mp[n].append(c)
            indegree[c] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        total = 0
        while q:
            curr = q.popleft()
            total += 1
            for nextC in mp[curr]:
                indegree[nextC] -= 1
                if indegree[nextC] == 0:
                    q.append(nextC)
        
        return total == numCourses
        

        


