class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        ret = 0
        for ind in range(len(timeSeries)-1):
            ret+=min(duration, timeSeries[ind+1]-timeSeries[ind])
        return ret+duration


sol = Solution()

timeSeries = [1,4]
duration = 2
print(sol.findPoisonedDuration(timeSeries, duration))