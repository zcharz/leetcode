class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new = []
        for i, inter in enumerate(intervals):
            if inter[1] < newInterval[0]:
                new.append(inter)
            elif inter[0] > newInterval[1]:
                new.append(newInterval)
                new.extend(intervals[i:])
                return new
            else:
                newInterval[0] = min(inter[0], newInterval[0])
                newInterval[1] = max(inter[1], newInterval[1])

        new.append(newInterval)        
        return new


sol = Solution()

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(sol.insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(sol.insert(intervals, newInterval))