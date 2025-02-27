# if sum(gas) < sum(cost), there cannot be a solution
# else there must be a solution

# since a solution exists, 
# if any starting point
# can iterate to the end of the list without being negative
# it must be the solution
# thus iterate from the start 
# where if the current running sum becomes less than 0
# the start must be after this point
#   greedily, since total gas > total cost, 
#   if the first section is negative, the back must have some start value
#   such that the excess gas covers the first section 


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost): return -1
        start, curr = 0, 0

        for i in range(len(gas)):
            curr = curr + gas[i] - cost[i]
            if curr < 0: 
                start = i+1
                curr = 0
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