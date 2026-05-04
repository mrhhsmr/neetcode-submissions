"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start, x.end))
        if len(intervals) <= 1:
            return True

        prev = intervals[0]
        for i in range(1, len(intervals), 1):
            curr = intervals[i]
            if curr.start < prev.end:
                return False
            
            prev = curr
        
        return True


