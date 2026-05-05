class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        if len(intervals) < 2:
            return 0
        
        res = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] >= prev[1]:
                prev = curr
            else:
                res += 1
                #删除一个，留下结尾小的那个
                prev[1] = min(prev[1], curr[1])

        return res 