# minimum spanning tree
# each point, a theoretical connection to all other nodes exist
# create all theoretical connections O(n*n)
# sort by length O(n^2logn^2)
# union find to check for cycles, 
# adding only min edges that don't create a cycle 
# until all nodes are connected

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        pass

