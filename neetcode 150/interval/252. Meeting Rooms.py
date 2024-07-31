class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
    
        return True


sol = Solution()

intervals = [(0,30),(5,10),(15,20)]
for i, (start, end) in enumerate(intervals):
    intervals[i] = Interval(start, end)
print(sol.canAttendMeetings(intervals))