class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = {}
        for i in range(numCourses):
            mp[i] = []
        
        for crs, pre in prerequisites:
            mp[pre].append(crs)
        
        visit = set()
        cycle = set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visit:
                return True
            
            cycle.add(crs)
            for nextCrs in mp[crs]:
                if dfs(nextCrs) == False:
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return res[::-1]
            


            