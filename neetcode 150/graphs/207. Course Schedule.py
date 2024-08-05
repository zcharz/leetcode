# CYCLE DETECTION
# DFS through prereqs, where each dfs sould end in a course with no prereq
# 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pass



    
sol = Solution()

numCourses = 2
prerequisites = [[1,0]]
print(sol.canFinish(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1,0],[0,1]]
print(sol.canFinish(numCourses, prerequisites))