class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        overlap = 0
        prevend = intervals[0][1]
        for start, end in intervals[1:]:
            if prevend > start:
                overlap+=1
                prevend = min(prevend, end)
            else:
                prevend = end
        return overlap

        

sol = Solution()

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(sol.eraseOverlapIntervals(intervals))

intervals = [[1,2],[1,2],[1,2]]
print(sol.eraseOverlapIntervals(intervals))

intervals = [[1,2],[2,3]]
print(sol.eraseOverlapIntervals(intervals))