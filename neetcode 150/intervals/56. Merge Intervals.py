class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ret = [intervals[0]]

        for inter in intervals[1:]:
            if ret[-1][1] >= inter[0]:
                ret[-1][1] = max(ret[-1][1], inter[1])
            else: 
                ret.append(inter)

        return ret


sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge(intervals))

intervals = [[1,4],[4,5]]
print(sol.merge(intervals))