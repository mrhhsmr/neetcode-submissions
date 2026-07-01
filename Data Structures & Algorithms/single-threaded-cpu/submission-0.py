class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key = lambda t:t[0])
        res, minh = [], []
        i, time = 0, tasks[0][0]
        
        while minh or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minh, [tasks[i][1], tasks[i][2]])
                i += 1
            if not minh:
                time = tasks[i][0]
            else:
                procT, index = heapq.heappop(minh)
                time += procT
                res.append(index)
        
        return res