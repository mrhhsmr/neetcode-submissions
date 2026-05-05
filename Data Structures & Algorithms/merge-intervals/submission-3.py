class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) == 0:
            return []
        
        prev = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if prev[1] < cur[0]:
                # only insert
                res.append(prev)
                prev = cur
            else:
                prev[0] = min(prev[0], cur[0])
                prev[1] = max(prev[1], cur[1])

        res.append(prev)
        return res
            