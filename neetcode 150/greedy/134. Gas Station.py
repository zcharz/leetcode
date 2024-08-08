# idea: if tank < 0, this cannot be starting point
# since a solution alawys exists, if any starting point
# can iterate to the end of the list without being negative
# it must be the solution (??)


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas)<sum(cost): return -1
        tank, start = 0, 0
        for i in range(len(gas)):
            tank += gas[i]-cost[i]
            if tank<0:
                tank = 0
                start = i+1
        return start




sol = Solution()

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(sol.canCompleteCircuit(gas, cost))

gas = [2,3,4]
cost = [3,4,3]
print(sol.canCompleteCircuit(gas, cost))

gas = [5,8,2,8]
cost = [6,5,6,6]
print(sol.canCompleteCircuit(gas, cost))

gas = [3,1,1]
cost = [1,2,2]
print(sol.canCompleteCircuit(gas, cost))