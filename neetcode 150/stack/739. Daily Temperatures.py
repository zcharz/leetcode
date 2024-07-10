class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ret = [0 for i in range(len(temperatures))]

        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                prev = stack.pop()
                ret[prev[1]] = i-prev[1]
            stack.append( (t, i) )
        return ret


sol = Solution()

temperatures = [73,74,75,71,69,72,76,73]
print(sol.dailyTemperatures(temperatures))

temperatures = [30,40,50,60]
print(sol.dailyTemperatures(temperatures))