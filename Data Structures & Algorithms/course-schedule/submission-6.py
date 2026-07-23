class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        mp = defaultdict(list)

        for curr, prev in prerequisites:
            mp[prev].append(curr)
            indegree[curr] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        res = 0
        while q:
            curr = q.popleft()
            res += 1
            for nextCourse in mp[curr]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:   
                    q.append(nextCourse)

        return res == numCourses