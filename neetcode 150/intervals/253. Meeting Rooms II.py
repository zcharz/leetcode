# Premium problem
# solved on Neetcode.io

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res, curr, s, e = 0, 0, 0, 0

        while s<len(intervals):
            if start[s] < end[e]: 
                s+=1
                curr+=1
            else:
                e+=1
                curr-=1
            res = max(res, curr)
        return res
    

sol = Solution()

intervals = [Interval(0,40), Interval(5,10), Interval(15,20)]
print(sol.minMeetingRooms(intervals))

intervals = [Interval(4,9)]
print(sol.minMeetingRooms(intervals))