class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        pass

sol = Solution()

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(sol.insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(sol.insert(intervals, newInterval))